# Python serialization benchmark

A simple serialization benchmark for textual data and NumPy arrays. Results
are obtained using `time.time_ns()`, and they are printed in nanoseconds.

## Libraries

- Avro
- `json` (standard library)
- orjson
- pickle4
- pickle5
- Protocol Buffers
- RapidJSON

## Running the benchmark

```bash
podman run --interactive --tty --rm \
	-v .:/home \
	-w /home \
	--env BENCHMARK_DATA_SIZE=$SIZE \
	--env BENCHMARK_ITERATIONS=$ITERATIONS \
	python:$PY_VERSION \
	sh -c "./run_benchmark.sh"
```

## Data type

`--env BENCHMARK_TYPE=...`

- `numeric` : See `benchmark/run/numeric_benchmark.py`
- `textual` : See `benchmark/run/textual_benchmark.py`

## Output

### CSV

`--env BENCHMARK_PP=csv` (default)
```
Serialization
Avro,Json,Orjson,Pickle4,Pickle5,Protobuf,RapidJSON
290244.85,26887717.19,1806935.09,48814.31,34544.63,78751.63,28539102.41

Deserialization
Avro,Json,Orjson,Pickle4,Pickle5,Protobuf,RapidJSON
105083.1,11868387.1,2163872.31,19100.97,22108.22,33005.58,12793808.94
```

### PGFPlots

`--env BENCHMARK_PP=pgfplot_histogram`
```
Serialization
(AvroBackend,284676.57) (JsonBackend,28447828.45) (OrjsonBackend,2088943.27) (Pickle4Backend,50752.19) (Pickle5Backend,39036.18) (ProtobufBackend,82686.77) (RapidjsonBackend,31793210.02)
Deserialization
(AvroBackend,113478.34) (JsonBackend,12809206.11) (OrjsonBackend,2546817.87) (Pickle4Backend,20552.24) (Pickle5Backend,24479.14) (ProtobufBackend,34602.56) (RapidjsonBackend,14472453.05)
```

## Results aggregation

`--env BENCHMARK_AGGREGATION=...`

- `mean` : Mean
- `min`/`max`: Min/max
- `percentile99`: 99th percentile
