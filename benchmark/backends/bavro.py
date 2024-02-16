from __future__ import annotations

from dataclasses import asdict
from io import BytesIO
from typing import Type

import avro.io
import avro.schema
import numpy as np

from benchmark.base import Backend
from benchmark.cases import Information, NumericArrayObject, TextObject

from .utils import numpy_array_as_bytes_and_dtype

schema = avro.schema.parse(open("benchmark/resources/message.avsc", "r").read())
writer = avro.io.DatumWriter(schema)


def _prepare_serializable_dict(dc: dict[str, object]) -> dict[str, object]:
    serializable_dc = {}
    for key, value in dc.items():
        if isinstance(value, np.ndarray):
            bytes_and_dtype = numpy_array_as_bytes_and_dtype(value)
            value = {"array": bytes_and_dtype.array, "dtype": bytes_and_dtype.dtype}
        serializable_dc[key] = value
    return serializable_dc


def _handle_fields(dc: dict[str, object]) -> dict[str, object]:
    deserialized_dc = {}
    for key, value in dc.items():
        if isinstance(value, dict):
            if "dtype" in value:
                dtype = np.lib.format.descr_to_dtype(value["dtype"])
                value = np.frombuffer(value["array"], dtype=dtype)
            elif "author" in value:
                value = Information(**value)
            else:
                raise ValueError(f"Unexpected dict: {value}")
        deserialized_dc[key] = value
    return deserialized_dc


class AvroBackend(Backend[bytes]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> bytes:
        bytes_writer = BytesIO()
        encoder = avro.io.BinaryEncoder(bytes_writer)
        writer.write(_prepare_serializable_dict(asdict(obj)), encoder)
        return bytes_writer.getvalue()

    @classmethod
    def deserialize(
        cls, serialized: bytes, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        bytes_reader = BytesIO(serialized)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(schema)
        dc = reader.read(decoder)
        return target_type(**_handle_fields(dc))

    @classmethod
    def label(cls) -> str:
        return "Avro"
