package com.example.client.controller;

import org.springframework.http.MediaType;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import com.example.client.rpcservice.BookProto.Book;
import com.example.client.rpcservice.BookProto.BookRequest;
import com.example.client.rpcservice.BookProto.BookResponse;
import com.example.client.rpcservice.BookProto.BooksResponse;
import com.example.client.rpcservice.BookServiceGrpc;
import com.googlecode.protobuf.format.JsonFormat;

import io.grpc.ManagedChannel;
@RestController
public class BookController {

    private ManagedChannel channelToPythonServer;
    private final BookServiceGrpc.BookServiceBlockingStub bookStub;

    BookController(ManagedChannel managedChannel) {
        channelToPythonServer = managedChannel;
        bookStub =  BookServiceGrpc.newBlockingStub(channelToPythonServer);
    }

    @GetMapping(value="/book/id/{id}", produces = MediaType.APPLICATION_JSON_VALUE)
    public String selectBookInfoById(@PathVariable int id) {
        Book book = Book.newBuilder().setId(id).build();

        BookResponse bookResponse = bookStub.getBook(
            BookRequest.newBuilder()
                .setBook(book)
                .build()
        );

        return new JsonFormat().printToString(bookResponse);
    }

    @GetMapping(value="/book/name/{name}", produces = MediaType.APPLICATION_JSON_VALUE)
    public String selectBooksByBookName(@PathVariable String name) {
        Book book = Book.newBuilder().setName(name).build();

        BooksResponse booksResponse = bookStub.getBooksByBookName(
            BookRequest.newBuilder()
                .setBook(book)
                .build()
        );

        return new JsonFormat().printToString(booksResponse);
    }
    
}
