#!/usr/bin/env bash

ENDPOINT="http://localhost:8000/extract"

# Send the files to the endpoint
curl -X POST $ENDPOINT \
     -F "pdf=@scanned-mail.pdf" \
     -F "prompt=@instructions.txt" \
     -F "json_schema=@schema.json"