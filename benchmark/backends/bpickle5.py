from __future__ import annotations

from pickle import dumps, loads
from typing import Type

from benchmark.base import Backend
from benchmark.cases import NumericArrayObject, TextObject


class Pickle5Backend(Backend[bytes]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> bytes:
        return dumps(obj, protocol=5)

    @classmethod
    def deserialize(
        cls, serialized: bytes, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        return loads(serialized)

    @classmethod
    def label(cls) -> str:
        return "Pickle5"
