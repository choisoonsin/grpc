import data_storage

import book_pb2
import book_pb2_grpc

book_db = data_storage.get_book_data()

success_message = {
    "response_code": "200",
    "response_msg": "it has been successfully done"
}


class BookService(book_pb2_grpc.BookServiceServicer):

    def GetBook(self, request, context):
        res = book_pb2.BookResponse(
            book=book_pb2.Book(**book_db[request.book.id]),
            **success_message
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
