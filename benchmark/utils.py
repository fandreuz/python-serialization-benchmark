from __future__ import annotations

import importlib
import inspect
from typing import Type

from benchmark.base import Backend


def get_all_backends() -> tuple[Type[Backend]]:
    return tuple(
        cls
        for _, cls in inspect.getmembers(
            importlib.import_module("benchmark.backends"), inspect.isclass
        )
    )
