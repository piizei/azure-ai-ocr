import json
import os
import tempfile
from typing import Annotated
from dotenv import load_dotenv
from starlette.responses import JSONResponse, Response
load_dotenv()
import uvicorn

from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel

from ai_ocr.chains import get_structured_data
from ai_ocr.process import process_pdf

app = FastAPI()




class ExtractionInput(BaseModel):
    pdf: UploadFile = File(...)
    prompt: UploadFile = File(...)
    json_schema: UploadFile = File(...)


class ExtractionOutput(BaseModel):
    structured_data: dict


@app.post("/extract")
async def extract(
        pdf: Annotated[UploadFile, File(...)],
        prompt: Annotated[UploadFile, File(...)],
        json_schema: Annotated[UploadFile, File(...)]

):
    pdf = await pdf.read()
    prompt = await prompt.read()
    json_schema = await json_schema.read()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(pdf)
        tmp_file_name = tmp.name
    try:
        response = process_pdf(file_to_ocr=tmp_file_name,
                       prompt=prompt.decode(),
                       json_schema=json_schema.decode())
    except Exception as e:
        response = {"error": str(e)}
    os.remove(tmp_file_name)
    return Response(content=json.dumps(response), media_type='application/json')

@app.post("/extract/{type}")
async def extract_type(
        pdf: Annotated[UploadFile, File(...)],
        prompt: Annotated[UploadFile, File(...)],
        json_schema: Annotated[UploadFile, File(...)],
        type: str
):
    file = await pdf.read()
    prompt = await prompt.read()
    json_schema = await json_schema.read()
    with tempfile.NamedTemporaryFile(delete=False, suffix=f".{type}") as tmp:
        tmp.write(pdf)
        tmp_file_name = tmp.name
    response = process_pdf(file_to_ocr=tmp_file_name,
                       prompt=prompt.decode(),
                       json_schema=json_schema.decode(),
                       type=type)
    os.remove(tmp_file_name)
    return Response(content=json.dumps(response), media_type='application/json')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
