import logging
import asyncio
from grpc import aio
from concurrent import futures

import book_service

import grpc
import book_pb2_grpc


async def serve():
    server = aio.server(futures.ThreadPoolExecutor(max_workers=10))
    book_pb2_grpc.add_BookServiceServicer_to_server(
        book_service.BookService(), server)
    server.add_insecure_port('[::]:50051')
    await server.start()
    await server.wait_for_termination()

    print('test')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
