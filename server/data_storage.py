import book_pb2


def get_book_data():
    return {
        1: {
            "id": 1,
            "name": "Who moved my cheese",
            "genre": book_pb2.Book.ROMANCE,
            "tags": ["motivational fable"],
            "author": {
                "id": 2,
                "name": "Cheese",
                "dob": "19800502"
            }
        },
        2: {
            "id": 2,
            "name": "The Giver",
            "genre": book_pb2.Book.MYSTERY,
            "tags": ["newbery", "science"],
            "author": {
                "id": 1,
                "name": "Louis",
                "dob": "19760502"
            }
        },
        3: {
            "id": 3,
            "name": "Who are you",
            "tags": ["netflix", "movie", "novel"],
            "author": {
                "id": 1,
                "name": "Louis",
                "dob": "19760502"
            }
        }
    }


if __name__ == '__main__':
    db = get_book_data()
    result = [db[i] for i in db if db[i]["name"].lower().find("who") != -1]
    print(result)
