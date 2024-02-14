from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class Information:
    name: str
    description: str
    id: int
    author: str


@dataclass(frozen=True, eq=False)
class NumericArrayObject:
    information: Information

    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    values: np.ndarray

    def __eq__(self, other):
        if not isinstance(other, NumericArrayObject):
            return False
        if not self.information == other.information:
            return False
        names = ("x", "y", "z", "values")
        return all(
            (
                np.array_equal(
                    getattr(self, name), getattr(other, name), equal_nan=True
                )
                for name in names
            )
        )


@dataclass(frozen=True)
class TextObject:
    information: Information

    abstract: str
    text: str
    appendix: str
