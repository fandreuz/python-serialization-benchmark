from __future__ import annotations

from dataclasses import asdict
from json import dumps, loads
from typing import Type

import numpy as np

from benchmark.base import Backend
from benchmark.cases import NumericArrayObject, TextObject


class JsonBackend(Backend[str]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> str:
        dc = asdict(obj)
        serializable_dc = {}
        for key, value in dc.items():
            if isinstance(value, np.ndarray):
                value = value.tolist()
            serializable_dc[key] = value
        return dumps(serializable_dc, default=str)

    @classmethod
    def deserialize(
        cls, serialized: str, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        dc = loads(serialized)
        deserialized_dc = {}
        for key, value in dc.items():
            if isinstance(value, (list, tuple)):
                value = np.array(value)
            deserialized_dc[key] = value
        return target_type(**deserialized_dc)
