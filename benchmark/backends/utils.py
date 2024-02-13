from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def as_serializable_dict(dc: dict[str, object]) -> dict[str, object]:
    serializable_dc = {}
    for key, value in dc.items():
        if isinstance(value, np.ndarray):
            value = value.tolist()
        serializable_dc[key] = value
    return serializable_dc


def handle_numpy_fields(dc: dict[str, object]) -> dict[str, object]:
    deserialized_dc = {}
    for key, value in dc.items():
        if isinstance(value, (list, tuple)):
            value = np.array(value)
        deserialized_dc[key] = value
    return deserialized_dc


@dataclass(frozen=True)
class SerializableNumPyArray:
    array: bytes
    dtype: str


def numpy_array_as_bytes_and_dtype(array: np.ndarray) -> SerializableNumPyArray:
    return SerializableNumPyArray(
        array.tobytes(), np.lib.format.dtype_to_descr(array.dtype)
    )
