import streamlit as st
import os
from dotenv import load_dotenv, set_key

# Load current environment variables
load_dotenv()

# Define the environment variables to be edited
env_vars = ["DOC_INTEL_ENDPOINT", "DOC_INTEL_KEY", "OPENAI_API_VERSION", "AZURE_OPENAI_ENDPOINT",
            "AZURE_OPENAI_API_DEPLOYMENT", "AZURE_OPENAI_API_KEY"]

# Create a dictionary to store the Streamlit input fields
input_fields = {}

st.title("Edit Environment Variables")

# Create an input field for each environment variable
for var in env_vars:
    current_value = os.getenv(var)
    input_fields[var] = st.text_input(f"Enter {var}", value=current_value)

# When the button is clicked, save the new values to the .env file
if st.button("Save"):
    for var, field in input_fields.items():
        new_value = field
        set_key(".env", var, new_value)
    st.success("Environment variables updated successfully!")
