package com.example.client.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class BookController {
 
    @GetMapping(value="/book/{id}")
    @ResponseBody
    public String selectBookInfoById(@PathVariable String id) {
        System.out.println("id ["+id+"]");

        return id;
    }
    
}
