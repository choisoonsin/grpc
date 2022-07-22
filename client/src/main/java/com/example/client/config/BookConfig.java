package com.example.client.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;

@Configuration
public class BookConfig {
    
    @Bean
    public ManagedChannel getManagedChannel() {
        return ManagedChannelBuilder.forTarget("127.0.0.1:50051")
                .usePlaintext()
                .build();
    }

}
