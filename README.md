Install dependencies:

```
pip install grpcio
pip install grpcio-tools
```

After creating .proto file, run this command:

`python -m grpc_tools.protoc -I./protos protos.test.proto --python_out=. --grpc_python_out=.`

tbd.
