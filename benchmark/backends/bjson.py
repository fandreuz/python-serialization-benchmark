from __future__ import annotations

from dataclasses import asdict
from json import dumps, loads
from typing import Type

from benchmark.base import Backend
from benchmark.cases import NumericArrayObject, TextObject


class JsonBackend(Backend[str]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> str:
        return dumps(asdict(obj), default=str)

    @classmethod
    def deserialize(
        cls, serialized: str, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        return target_type(**loads(serialized))
