import numpy as np
import pytest

from benchmark.backends import *
from benchmark.base import Backend
from benchmark.cases import Information, NumericArrayObject, TextObject

x = np.linspace(0, 1, 10)
y = np.linspace(-1, 1, 10)
z = np.linspace(0, 1, 10)
values = np.random.rand(10)

info = Information("Test", "My test", 0, "fandreuz@cern.ch")


@pytest.mark.parametrize(
    "value",
    (
        NumericArrayObject(info, x, y, z, values),
        TextObject(info, "My abstract", "Lorem ipsum", "Appendix something"),
    ),
)
@pytest.mark.parametrize(
    "backend",
    (
        AvroBackend,
        JsonBackend,
        OrjsonBackend,
        Pickle4Backend,
        Pickle5Backend,
        ProtobufBackend,
        RapidjsonBackend,
    ),
)
def test_round_trip(value, backend: Backend):
    result = backend.deserialize(backend.serialize(value), type(value))

    print(f"Expected: {value}")
    print(f"Result: {result}")
    assert value == result
