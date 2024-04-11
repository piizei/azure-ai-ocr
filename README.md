# AI OCR with Azure

## This project demonstrates 'autopilot' OCR with Azure Cognitive Services

Classic OCR models need training to extract structured information from documents.
In this project I demonstrate how to use hybrid approach with LLM (multimodal) to get better results without any pre-training.

## How to use
Run example projects in `examples-*` folder.

The examples need docker to run. Each folder has a script that you can execute to run the complete example.
Each folder has also .env file that needs to be filled with your Azure service credentials.



### Example 1
[example 1 - Sample collection](example-1-sample-collection) Extract process of water sample providing from an information flyer.



## Develop

Install with poetry

```bash
poetry install
```
