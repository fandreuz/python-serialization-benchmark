from __future__ import annotations

from dataclasses import asdict
from json import dumps, loads
from typing import Type

from benchmark.base import Backend
from benchmark.cases import NumericArrayObject, TextObject

from .utils import as_serializable_dict, handle_fields


class JsonBackend(Backend[str]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> str:
        dc = asdict(obj)
        return dumps(as_serializable_dict(dc), default=str)

    @classmethod
    def deserialize(
        cls, serialized: str, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        dc = loads(serialized)
        return target_type(**handle_fields(dc))
