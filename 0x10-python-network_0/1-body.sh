#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the  the body of the response
curl -s -X GET "$1" -L
