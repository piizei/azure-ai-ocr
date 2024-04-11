# Start the Docker container
Start-Process -NoNewWindow -FilePath "docker" -ArgumentList "run -d --name azure-ai-ocr --env-file .env.docker -p 8000:8000 ghcr.io/piizei/azure-ai-ocr:latest"

# Give the container a few seconds to start
Start-Sleep -Seconds 5

$ENDPOINT="http://localhost:8000/extract"

# Send the files to the endpoint
Invoke-WebRequest -Uri $ENDPOINT -Method POST -ContentType "multipart/form-data" -InFile @("scanned-mail.pdf", "instructions.txt", "schema.json") -OutFile $null

# Stop and remove the Docker container
Start-Process -NoNewWindow -FilePath "docker" -ArgumentList "stop azure-ai-ocr"
Start-Process -NoNewWindow -FilePath "docker" -ArgumentList "rm azure-ai-ocr"