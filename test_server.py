from concurrent import futures
import grpc
import test_pb2
import test_pb2_grpc
from test_pb2 import Unit

KM_IN_MILE = 1.609344

class ConverterService(test_pb2_grpc.ConverterServiceServicer): # here we inherit the service and its method
    def convertUnits(self, request, context): # inside this method we define the logic
        if request.category == Unit.KILOMETERS:
            result = request.input / KM_IN_MILE
            return test_pb2.UnitResponse(result=result, unit=Unit.Name(1))
        elif request.category == Unit.MILES:
            result = request.input * KM_IN_MILE
            return test_pb2.UnitResponse(result=result, unit=Unit.Name(0))
        else:
            raise NotImplementedError('Not implemented!')

def main():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10)) # can take 10 concurrent requests
    test_pb2_grpc.add_ConverterServiceServicer_to_server(ConverterService(), server)
    server.add_insecure_port('[::]:50052')
    print("Server is running..")
    server.start()
    server.wait_for_termination()

main()