package com.example.client.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.client.rpcservice.BookProto.Book;
import com.example.client.rpcservice.BookServiceGrpc;
import com.googlecode.protobuf.format.JsonFormat;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
@RestController
public class BookController {

    @GetMapping(value="/book/{id}")
    @ResponseBody
    public String selectBookInfoById(@PathVariable int id) {
        System.out.println("id ["+id+"]");

        Book book = Book.newBuilder()
            .setId(id)   
            .build();

        ManagedChannel channel = ManagedChannelBuilder.forTarget("127.0.0.1:50051")
            .usePlaintext()
            .build();

        BookServiceGrpc.BookServiceBlockingStub stub =  BookServiceGrpc.newBlockingStub(channel);
        Book response = stub.getBook(book);

        return new JsonFormat().printToString(response);
    }
    
}
