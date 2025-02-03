package main

import (
	"log"
	"context"
	"logservice/gen-go/log_service"
	"github.com/apache/thrift/lib/go/thrift"
)

func main(){
	transport, err := thrift.NewTSocket("localhost:9090")
	if err != nil {
		log.Fatalf("Error creating transport: %v", err)
	} else {
		log.Println("Transport created")
	}
	defer transport.Close()
	
	if err := transport.Open(); err != nil {
		log.Fatalf("Error opening transport: %v", err)
	} else {
		log.Println("Transport opened")
	}
	
	protocolFactory := thrift.NewTBinaryProtocolFactoryDefault()
	protocol := protocolFactory.GetProtocol(transport)
	client := log_service.NewLogServiceClientProtocol(transport, protocol,protocol)
	ctx := context.Background()
	filePath := "/tmp/test.log"
	
	result, err := client.ReadLogFile(ctx, filePath) 
	if err != nil {
		log.Fatalf("Error calling ReadLogFile: %v", err)
	}
	log.Println("ReadLogFile result:", result)
}
