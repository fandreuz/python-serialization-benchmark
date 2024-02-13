from __future__ import annotations

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
