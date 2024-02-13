from __future__ import annotations

from typing import Type

import numpy as np

from benchmark.base import Backend
from benchmark.cases import Information, NumericArrayObject, TextObject

from .generated.message_pb2 import (
    NumericArrayObjectMsg,
    NumPyMsg,
    TextObjectMsg,
)
from .utils import numpy_array_as_bytes_and_dtype


def _pack_numpy_array(array: np.ndarray, msg: NumPyMsg):
    bytes_and_dtype = numpy_array_as_bytes_and_dtype(array)
    msg.array = bytes_and_dtype.array
    msg.dtype = bytes_and_dtype.dtype


def _unpack_numpy_array(msg: NumPyMsg) -> np.ndarray:
    dtype = np.lib.format.descr_to_dtype(msg.dtype)
    return np.frombuffer(msg.array, dtype=dtype)


class ProtobufBackend(Backend[bytes]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> bytes:
        if isinstance(obj, NumericArrayObject):
            msg = NumericArrayObjectMsg()
            _pack_numpy_array(obj.x, msg.x)
            _pack_numpy_array(obj.y, msg.y)
            _pack_numpy_array(obj.z, msg.z)
            _pack_numpy_array(obj.values, msg.values)
        else:
            msg = TextObjectMsg()
            msg.abstract = obj.abstract
            msg.text = obj.text
            msg.appendix = obj.appendix

        msg.information.name = obj.information.name
        msg.information.description = obj.information.description
        msg.information.id = obj.information.id
        msg.information.author = obj.information.author
        msg.information.generated_at.FromDatetime(obj.information.generated_at)

        return msg.SerializeToString()

    @classmethod
    def deserialize(
        cls, serialized: bytes, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        if target_type == NumericArrayObject:
            msg = NumericArrayObjectMsg()
        else:
            msg = TextObjectMsg()
        msg.ParseFromString(serialized)

        information = Information(
            name=msg.information.name,
            description=msg.information.description,
            id=msg.information.id,
            author=msg.information.author,
            generated_at=msg.information.generated_at.ToDatetime(),
        )

        if target_type == NumericArrayObject:
            return NumericArrayObject(
                information=information,
                x=_unpack_numpy_array(msg.x),
                y=_unpack_numpy_array(msg.y),
                z=_unpack_numpy_array(msg.z),
                values=_unpack_numpy_array(msg.values),
            )
        return TextObject(
            information=information,
            abstract=msg.abstract,
            text=msg.text,
            appendix=msg.abstract,
        )
