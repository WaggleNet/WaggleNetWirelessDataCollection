package main

import (
    "fmt"
    "io"
	"os"
    "net/http"
)

func uploadFile(w http.ResponseWriter, r *http.Request) {
    fmt.Println("File Upload Endpoint Hit")

    // Parse our multipart form, 10 << 20 specifies a maximum
    // upload of 10 MB files.
    r.ParseMultipartForm(10 << 20)
    // FormFile returns the first file for the given key `myFile`
    // it also returns the FileHeader so we can get the Filename,
    // the Header and the size of the file
    file, handler, err := r.FormFile("myFile")
    if err != nil {
        fmt.Println("Error Retrieving the File")
        fmt.Println(err)
        return
    }
    defer file.Close()
    fmt.Printf("Uploaded File: %+v\n", handler.Filename)
    fmt.Printf("File Size: %+v\n", handler.Size)
    fmt.Printf("MIME Header: %+v\n", handler.Header)

	// Open the destination file in append mode
    destFile, err := os.OpenFile("temp/upload.log", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        fmt.Println("Error opening destination file")
		fmt.Println(err)
        return
    }
    defer destFile.Close()

    // Copy the uploaded file's content directly to upload.txt
    if _, err := io.Copy(destFile, file); err != nil {
        fmt.Println("Error saving file")
		fmt.Println(err)
        return
    }

    fmt.Fprintf(w, "Successfully Uploaded File\n")
}

func setupRoutes() {
    http.HandleFunc("/upload", uploadFile)
    http.ListenAndServe(":8080", nil)
}

func main() {
    fmt.Println("Hello World")
    setupRoutes()
}
