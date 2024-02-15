set -uex

python -m pip install .
python -m pip install grpcio-tools
mkdir benchmark/backends/generated
python -m grpc_tools.protoc \
       -I=benchmark/resources \
       --python_out=benchmark/backends/generated/ \
       benchmark/resources/message.proto
python -m benchmark.run.${BENCHMARK_TYPE}_benchmark