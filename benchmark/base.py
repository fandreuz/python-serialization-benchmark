from __future__ import annotations

import abc
from typing import Generic, Type, TypeVar

from .cases import NumericArrayObject, TextObject

S = TypeVar("S")


class Backend(Generic[S]):
    @classmethod
    @abc.abstractmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> S:
        pass

    @classmethod
    @abc.abstractmethod
    def deserialize(
        cls, serialized: S, target_type: Type[TextObject | NumericArrayObject]
    ) -> TextObject | NumericArrayObject:
        pass
