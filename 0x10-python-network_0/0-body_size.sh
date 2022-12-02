#!/bin/bash
#this bash script takes in a URL, sends a request to the URL, and also displays the size of the body of the response.
curl -sI "$1" | grep Content-Length | cut -d " " -f2
