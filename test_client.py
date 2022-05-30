import grpc
import test_pb2
import test_pb2_grpc
from test_pb2 import Unit

def run():
    with grpc.insecure_channel('0.0.0.0:50052') as channel:
        stub = test_pb2_grpc.ConverterServiceStub(channel)
        response = stub.convertUnits(test_pb2.UnitRequest(input=100.55, category=Unit.KILOMETERS))
        print(response.result, " ", response.unit)

if __name__ == '__main__':
    run()