import numpy as np

from benchmark.cases import Information, NumericArrayObject
from benchmark.run.base import run_backends, pretty_print


def generate_obj(size):
    x = np.linspace(0, 1, size)
    y = np.linspace(-1, 1, size)
    z = np.linspace(0, 1, size)
    values = np.random.rand(size)
    info = Information(
        "Numeric benchmark", "Data for numeric benchmark", 0, "fandreuz@cern.ch"
    )
    return NumericArrayObject(information=info, x=x, y=y, z=z, values=values)


if __name__ == "__main__":
    pretty_print(run_backends(generate_obj))
