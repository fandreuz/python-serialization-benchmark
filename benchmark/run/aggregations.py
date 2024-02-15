from __future__ import annotations

from functools import partial
from typing import Callable, TypeAlias, cast

import numpy as np

Aggregation: TypeAlias = Callable[[np.ndarray], float]


def _percentile99(value: np.ndarray):
    return np.percentile(value, 99)


aggregations: dict[str, Aggregation] = {
    "mean": cast(Aggregation, np.mean),
    "max": cast(Aggregation, np.max),
    "min": cast(Aggregation, np.min),
    "percentile99": cast(Aggregation, partial(np.percentile, q=99)),
}
