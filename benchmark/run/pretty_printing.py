from __future__ import annotations

import sys
from typing import Callable, Sequence, cast

if sys.version_info >= (3, 10):
    from typing import TypeAlias
else:
    from typing_extensions import TypeAlias

from benchmark.run.aggregations import Aggregation
from benchmark.run.model import BackendResult

PrettyPrinting: TypeAlias = Callable[[Sequence[BackendResult], Aggregation], None]


def _print_backends(results: Sequence[BackendResult]):
    print(",".join(result.backend.label() for result in results))


def _csv(results: Sequence[BackendResult], aggregation: Aggregation):
    print("Serialization")
    _print_backends(results)
    print(
        ",".join(str(aggregation(result.serialization_times_ns)) for result in results)
    )

    print("Deserialization")
    _print_backends(results)
    print(
        ",".join(
            str(aggregation(result.deserialization_times_ns)) for result in results
        )
    )


def _pgfplot_histogram(results: Sequence[BackendResult], aggregation: Aggregation):
    print("Serialization")
    print(
        " ".join(
            f"({result.backend.label()},{aggregation(result.serialization_times_ns)})"
            for result in results
        )
    )

    print("Deserialization")
    print(
        " ".join(
            f"({result.backend.label()},{aggregation(result.deserialization_times_ns)})"
            for result in results
        )
    )


pretty_printings: dict[str, PrettyPrinting] = {
    "csv": cast(PrettyPrinting, _csv),
    "pgfplot_histogram": cast(PrettyPrinting, _pgfplot_histogram),
}
