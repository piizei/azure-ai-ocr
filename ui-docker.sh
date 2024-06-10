#!/usr/bin/env bash
# This script is used to start the UI
docker run --name azure-ai-ocr-ui --env-file .env.docker -p 8501:8501 ghcr.io/piizei/azure-ai-ocr-ui:latest
