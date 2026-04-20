package main

import (
	"fmt"
	"log"
	"net/http"
	"os"
)

func main() {
	// Get port from environment or default to 3000
	port := os.Getenv("PORT")
	if port == "" {
		port = "3000"
	}

	// Health check endpoint
	http.HandleFunc("/healthz", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		fmt.Fprint(w, "OK")
	})

	// Sample endpoint
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		logLevel := os.Getenv("LOG_LEVEL")
		fmt.Fprintf(w, "Hello from %s! (Log Level: %s)\n", "my-awesome-app", logLevel)
	})

	fmt.Printf("Starting server on port %s...\n", port)
	if err := http.ListenAndServe(":"+port, nil); err != nil {
		log.Fatalf("Server failed: %s", err)
	}
}
