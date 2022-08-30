import data_storage
import asyncio

import book_pb2
import book_pb2_grpc

import time

book_db = data_storage.get_book_data()

success_message = {
    "response_code": "200",
    "response_msg": "it has been successfully done"
}

not_found_message = {
    "response_code": "404",
    "response_msg": "No data found"
}

fail_message = {
    "response_code": "500",
    "response_msg": "Occured a server error"
}


def exec_dnn_learning():
    time.sleep(3)

    # f = open("test.txt", "w")
    # for i in range(1000, 4000):
    #     f.write(str(pow(i, i)) + "\n")
    # f.close()

    print("Learning dnn model has been finished")


class BookService(book_pb2_grpc.BookServiceServicer):

    async def GetHello(self, request, context):
        loop = asyncio.get_event_loop()
        # await loop.run_in_executor(None, exec_dnn_learning)
        loop.run_in_executor(None, exec_dnn_learning)

        print(request)
        res = book_pb2.SimpleStringMessage(message=request.message)
        return res

    def GetBookById(self, request, context):
        try:
            res = book_pb2.BookResponse(
                book=book_pb2.Book(**book_db[request.book.id]),
                **success_message
            )
        except KeyError:
            res = book_pb2.BookResponse(
                **not_found_message
            )
        except:
            res = book_pb2.BookResponse(
                **fail_message
            )

        return res

    def GetBooksByBookName(self, request, context):

        book_name = request.book.name.lower()

        if len(book_name) < 2:
            return book_pb2.BooksResponse(
                response_code="500",
                response_msg="Please put name at least 3 characters"
            )

        res = book_pb2.BooksResponse(
            books=[
                book_db[i] for i in book_db if book_db[i]["name"].lower().find(book_name) != -1
            ],
            **success_message
        )
        return res

    def GetAllContents(self, request, context):
        contents = [
            """
                Page 1.
                Greeting
            """,
            """
                Page 2.
                Nice to meet you
            """,
            """
                Page 3.
                See you later
            """,
            """
                Page 4.
                bye
            """
        ]

        for content in contents:
            time.sleep(1)
            yield book_pb2.SimpleStringMessage(message=content)

    def SetAllContents(self, request_iterator, context):
        for request in request_iterator:
            print(request.message)

        return book_pb2.SimpleStringMessage(message="200")

    def StreamAllBooksById(self, request_iterator, context):
        for request in request_iterator:
            print(request.id)

            yield book_pb2.Book(**book_db[request.id])
