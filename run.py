from datetime import datetime

import numpy as np

from benchmark.backends.bjson import JsonBackend
from benchmark.cases import Information, NumericArrayObject

x = np.linspace(0, 1, 10)
y = np.linspace(-1, 1, 10)
z = np.linspace(0, 1, 10)
values = np.random.rand(10)

info = Information("Test", "My test", 0, "fandreuz@cern.ch", datetime.now())
obj = NumericArrayObject(info, x, y, z, values)
print(JsonBackend.serialize(obj))
