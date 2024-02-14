from __future__ import annotations

from dataclasses import asdict
from typing import Type

from orjson import dumps, loads

from benchmark.base import Backend
from benchmark.cases import NumericArrayObject, TextObject

from .utils import as_serializable_dict, handle_fields


class OrjsonBackend(Backend[bytes]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> bytes:
        dc = asdict(obj)
        return dumps(as_serializable_dict(dc), default=str)

    @classmethod
    def deserialize(
        cls, serialized: bytes, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        dc = loads(serialized)
        return target_type(**handle_fields(dc))
