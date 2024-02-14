from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Information:
    name: str
    description: str
    id: int
    author: str


@dataclass(frozen=True)
class NumericArrayObject:
    information: Information

    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    values: np.ndarray


@dataclass(frozen=True)
class TextObject:
    information: Information

    abstract: str
    text: str
    appendix: str
