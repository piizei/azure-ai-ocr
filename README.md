# AI OCR with Azure

## This project demonstrates 'autopilot' OCR with Azure Cognitive Services

Classic OCR models need training to extract structured information from documents.
In this project I demonstrate how to use hybrid approach with LLM (multimodal) to get better results without any pre-training.

The project uses Azure Document Intelligence combined with GPT4 and GPT-Vision. Each of the tools have their strong points and the hybrid approach is better than any of them alone.

Notes:
- The document-intelligence needs to be using the markdown preview (limited regions). 
- The openai model needs to be vision capable.

## How to use
Run example projects in `examples-*` folder.

The examples need docker to run. Each folder has a script that you can execute to run the complete example.
Each folder has also .env file that needs to be filled with your Azure service credentials.

*Complete the .env files in each example folder before running.*

Note: The powershell scripts don't work very well, the bash scripts are better...

### Example 1
[example 1 - Sample collection](example-1-sample-collection) Extract process of water sample providing from an information flyer.


### Example 2
[example 2 - Complex tables](example-2-tables) Let's find some insurance products from a more complex table.

### Notes on the examples
- I used https://bjdash.github.io/JSON-Schema-Builder/ to create the json-schemas in the example folders. If the keys in the json model are not self-explanatory, you should use description fields to tell the LLM model what you mean by each key to increase accuracy.


## User interface
User interface is provided for testing purposes only.
To run it locally, install 
```bash
poetry install --with ui
```
an run `./ui.sh` in the root folder. (env is picked from .env file in the root folder) 


## Develop

Install with poetry

```bash
poetry install
```
