from dataclasses import dataclass
from typing import Type

import numpy as np

from benchmark.base import Backend


@dataclass(frozen=True)
class Config:
    # Size of the relevant data (e.g. array length)
    size: int
    # Number of times the experiment shall be repeated
    count: int


@dataclass(frozen=True)
class BackendResult:
    backend: Type[Backend]
    serialization_times_ns: np.ndarray
    deserialization_times_ns: np.ndarray
