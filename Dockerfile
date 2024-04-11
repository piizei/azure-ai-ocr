FROM python:3.11-bookworm

# set work directory
WORKDIR /usr/src/app

# install dependencies
COPY pyproject.toml README.md ./
RUN pip install poetry && \
    poetry config virtualenvs.create false
COPY ai_ocr/ ai_ocr/
RUN poetry install
WORKDIR /usr/src/app

EXPOSE 8000
ENTRYPOINT ["python", "ai_ocr/main.py"]
