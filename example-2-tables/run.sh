#!/usr/bin/env bash
docker run -d --name azure-ai-ocr --env-file .env.docker -p 8000:8000 ghcr.io/piizei/azure-ai-ocr:latest > /dev/null 2>&1
sleep 5
ENDPOINT="http://localhost:8000/extract"


curl -s -S -X POST $ENDPOINT \
     -F "pdf=@hausrat.pdf" \
     -F "prompt=@instructions.txt" \
     -F "json_schema=@schema.json"

docker stop azure-ai-ocr > /dev/null 2>&1
docker rm azure-ai-ocr > /dev/null 2>&1