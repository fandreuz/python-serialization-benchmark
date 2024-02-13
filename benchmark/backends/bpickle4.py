from __future__ import annotations

from pickle import dumps, loads
from typing import Type

from benchmark.base import Backend
from benchmark.cases import NumericArrayObject, TextObject


class Pickle4Backend(Backend[bytes]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> bytes:
        return dumps(obj, protocol=4)

    @classmethod
    def deserialize(
        cls, serialized: bytes, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        return loads(serialized)
