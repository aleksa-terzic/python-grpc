pip install grpcio
pip install grpcio-tools

python -m grpc_tools.protoc -I./protos protos.test.proto --python_out=. --grpc_python_out=.

