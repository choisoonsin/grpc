from concurrent import futures
import logging

import grpc
import book_pb2
import book_pb2_grpc

class BookService(book_pb2_grpc.BookServiceServicer):

    def __init__(self):
        self.storage = {
            1:{
                "id":1,
                "name":"Who moved my cheese",
                "genre":book_pb2.Book.ROMANCE,
                "tags":["motivational fable"]
            },
            2:{
                "id":2,
                "name":"The Giver",
                "genre":book_pb2.Book.MYSTERY,
                "tags":["Newbery award", "science"]
            }
        }

    def GetBook(self, request, context):
        book = book_pb2.Book(**self.storage[request.id])
        return book

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServiceServicer_to_server(BookService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()