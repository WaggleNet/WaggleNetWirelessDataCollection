package main

import (
    "fmt"
    "net/http"
    "io/ioutil"
)

var s = ""

func uploadFile(w http.ResponseWriter, r *http.Request) {
        // Read the body of the request
        body, err := ioutil.ReadAll(r.Body)
        if err != nil {
            http.Error(w, "Error reading request body", http.StatusBadRequest)
            return
        }
    
        // Convert the body to a string
        bodyString := string(body)
    
        // Print the body string to the console
        //fmt.Println("Request Body:", bodyString)
        s += bodyString
        fmt.Println(s)
    
        // Send a response
        fmt.Fprintf(w, "%s", s)
    
}

func getFiles(w http.ResponseWriter, r *http.Request) {
    // Send a response
    fmt.Fprintf(w, "%s", s)

}

func setupRoutes() {
    http.HandleFunc("/upload", uploadFile)
    http.HandleFunc("/files", getFiles)
    http.ListenAndServe(":8080", nil)
}

func main() {
    fmt.Println("Hello World")
    setupRoutes()
}