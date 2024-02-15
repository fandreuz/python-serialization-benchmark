# Python serialization benchmark

A simple serialization benchmark for textual data and NumPy arrays.

### Libraries

- Avro
- `json` (standard library)
- orjson
- pickle4
- pickle5
- Protocol Buffers
- RapidJSON

### Running the benchmark

```bash
podman run --interactive --tty --rm \
	-v .:/home \
	-w /home \
        --env BENCHMARK_DATA_SIZE=$SIZE \    # data size (i.e. array length)
        --env BENCHMARK_ITERATIONS=$COUNT \  # number of measurements
        --env BENCHMARK_TYPE=numeric \       # or 'textual'
	python:$PY_VERSION \
	./run_benchmark.sh
```
