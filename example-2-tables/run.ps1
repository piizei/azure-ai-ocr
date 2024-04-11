# Start the Docker container
Start-Process -NoNewWindow -FilePath "docker" -ArgumentList "run -d --name azure-ai-ocr --env-file .env.docker -p 8000:8000 ghcr.io/piizei/azure-ai-ocr:latest"

# Give the container a few seconds to start
Start-Sleep -Seconds 5

$ENDPOINT="http://localhost:8000/extract"

# Send the files to the endpoint
cmd /c curl -s -S -X POST $ENDPOINT -F "pdf=@hausrat.pdf" -F "prompt=@instructions.txt" -F "json_schema=@schema.json"

# Stop and remove the Docker container
Start-Process -NoNewWindow -FilePath "docker" -ArgumentList "stop azure-ai-ocr"
Start-Process -NoNewWindow -FilePath "docker" -ArgumentList "rm azure-ai-ocr"