from __future__ import annotations

from ..base import Backend
from ..cases import NumericArrayObject, TextObject


class PickleBackend(Backend[bytes]):
    @classmethod
    def serialize(cls, obj: TextObject | NumericArrayObject) -> bytes:
        pass
