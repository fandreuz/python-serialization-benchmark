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
        --env BENCHMARK_DATA_SIZE=$SIZE \
        --env BENCHMARK_ITERATIONS=$COUNT \
	python:$PY_VERSION \
	sh -c "python -m pip install . ; python -m benchmark.run.numeric_benchmark"
```
