import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
from ai_ocr.azure.openai_ops import get_llm
from test_ui.prompt import create_schema
from ai_ocr.process import process_pdf
import tempfile
import pandas as pd
st.set_page_config(
    page_title="AI OCR",
    page_icon="👁",
    layout="wide",
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
# select-list filetype
st.write("Select the file type")
file_type = st.selectbox("File type", ["pdf", "png", "jpg", "docx"])

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None and instructions is not None:
    if st.button("Process"):
        with st.spinner('Processing...'):
            schema = create_schema(instructions)
            with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_type}") as tmp:
                tmp.write(uploaded_file.getvalue())
                tmp_file_name = tmp.name
                print(tmp_file_name)
            response = process_pdf(file_to_ocr= tmp_file_name,
                                   prompt=instructions,
                                   json_schema=schema,
                                   type=file_type)
            os.remove(tmp_file_name)
            if response:
                col1, col2 = st.columns(2)
                with col1:
                    try:
                        df = pd.DataFrame.from_dict(response)
                        st.table(df)
                    except:
                        try:
                            df = pd.DataFrame.from_dict(response, orient='index')
                            st.table(df)
                        except:
                            print(response)
                with col2:
                    st.json(response)

