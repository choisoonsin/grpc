package com.example.client.controller;

import java.util.Arrays;
import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import com.example.client.rpcservice.BookProto.Book;
import com.example.client.rpcservice.BookProto.Book.Genre;
import com.googlecode.protobuf.format.JsonFormat;
@RestController
public class BookController {
 
    @GetMapping(value="/book/{id}")
    @ResponseBody
    public String selectBookInfoById(@PathVariable int id) {
        System.out.println("id ["+id+"]");

        Book book = Book.newBuilder()
            .setId(id)   
            .setName("Jonny")
            .setGenre(Genre.ROMANCE)
            .addTags("romance").addTags("newbery award")
            .build(); 

        return new JsonFormat().printToString(book);
    }
    
}
