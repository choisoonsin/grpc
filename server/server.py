from concurrent import futures
import logging

import grpc
import book_pb2
import book_pb2_grpc

class BookService(book_pb2_grpc.BookServiceServicer):
    def GetBook(self, request, context):
        return book_pb2.Book(
            id=1,
            name='Bob',
            genre=book_pb2.Book.ACTION,
            tags=["romance", "human story"]
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()