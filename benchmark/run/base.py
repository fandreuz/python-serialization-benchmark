from __future__ import annotations

import os
import sys
import time
from typing import Callable, Type

import numpy as np

from benchmark.base import Backend
from benchmark.cases import NumericArrayObject, TextObject
from benchmark.run.aggregations import aggregations
from benchmark.run.model import BackendResult, Config
from benchmark.run.pretty_printing import pretty_printings
from benchmark.utils import get_all_backends


def _acquire_config() -> Config:
    data_size, benchmark_iterations = None, None
    if len(sys.argv) == 1:
        data_size = os.environ.get("BENCHMARK_DATA_SIZE")
        benchmark_iterations = os.environ.get("BENCHMARK_ITERATIONS")
    elif len(sys.argv) == 3:
        data_size = sys.argv[1]
        benchmark_iterations = sys.argv[2]

    if data_size is None or benchmark_iterations is None:
        raise ValueError("Benchmark parameters were not specified")

    return Config(int(data_size), int(benchmark_iterations))


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

    aggregation = aggregations.get(os.environ.get("BENCHMARK_AGGREGATION", "mean"))
    pp = pretty_printings.get(os.environ.get("BENCHMARK_PP", "csv"))

    pp(results_sorted, aggregation)
