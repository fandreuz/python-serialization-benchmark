from __future__ import annotations

import sys
import time
from dataclasses import dataclass
from typing import Callable, Type

import numpy as np

from benchmark.base import Backend
from benchmark.cases import NumericArrayObject, TextObject
from benchmark.utils import get_all_backends


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


def _acquire_config() -> Config:
    return Config(int(sys.argv[1]), int(sys.argv[2]))


def _measure(
    obj: NumericArrayObject | TextObject, count: int, backend: Type[Backend]
) -> BackendResult:
    serialization_times = np.empty(count, dtype=np.int64)
    deserialization_times = np.empty(count, dtype=np.int64)

    target_type = type(obj)
    for i in range(count):
        start = time.time_ns()
        s = backend.serialize(obj)
        middle = time.time_ns()
        d = backend.deserialize(s, target_type)  # noqa: F841
        end = time.time_ns()

        serialization_times[i] = middle - start
        deserialization_times[i] = end - middle

    return BackendResult(backend, serialization_times, deserialization_times)


def run_backends(
    obj_generator: Callable[
        [
            int,
        ],
        NumericArrayObject | TextObject,
    ],
) -> tuple[BackendResult]:
    config = _acquire_config()
    obj = obj_generator(config.size)
    return tuple(_measure(obj, config.count, backend) for backend in get_all_backends())


def pretty_print(results: tuple[BackendResult]):
    results_sorted = sorted(results, key=lambda result: str(result.backend))
    del results

    # Ready for LaTeX ;)
    print("Serialization")
    print(",".join(result.backend.__name__ for result in results_sorted))
    print(
        ",".join(
            str(np.mean(result.serialization_times_ns)) for result in results_sorted
        )
    )

    print("Deserialization")
    print(",".join(result.backend.__name__ for result in results_sorted))
    print(
        ",".join(
            str(np.mean(result.deserialization_times_ns)) for result in results_sorted
        )
    )
