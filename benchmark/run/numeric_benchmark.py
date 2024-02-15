import numpy as np

from benchmark.cases import Information, NumericArrayObject
from benchmark.run.base import pretty_print, run_backends


def generate_obj(size):
    x = np.linspace(0, 1, size, dtype=np.float64)
    y = np.linspace(-1, 1, size, dtype=np.float64)
    z = np.linspace(0, 1, size, dtype=np.float64)
    values = np.random.rand(size).astype(dtype=np.float64)
    info = Information(
        "Numeric benchmark", "Data for numeric benchmark", 0, "fandreuz@cern.ch"
    )
    return NumericArrayObject(information=info, x=x, y=y, z=z, values=values)


if __name__ == "__main__":
    pretty_print(run_backends(generate_obj))
