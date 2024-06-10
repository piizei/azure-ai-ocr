import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from ai_ocr.azure.openai_ops import get_llm
from test_ui.prompt import create_schema
from ai_ocr.process import process_pdf
import tempfile


st.set_page_config(
    page_title="AI OCR",
    page_icon="👁",
)

st.write("# Welcome to Azure AI Autopilot OCR")

st.markdown(
    """
    Processing instructions
"""
)
instructions = st.text_area("")
st.markdown(
    """
    Upload a file for OCR.
"""
)
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None and instructions is not None:
    if st.button("Process"):
        with st.spinner('Processing...'):
            schema = create_schema(instructions)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_file_name = tmp.name
                print(tmp_file_name)
            response = process_pdf(file_to_ocr= tmp_file_name,
                                   prompt=instructions,
                                   json_schema=schema)
            st.json(response)
            os.remove(tmp_file_name)
