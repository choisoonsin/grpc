import book_service

from concurrent import futures
import logging

import grpc
import book_pb2_grpc


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServiceServicer_to_server(
        book_service.BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

    print('test')


if __name__ == '__main__':
    logging.basicConfig()
    serve()
