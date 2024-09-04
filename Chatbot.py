import os
from api_key import llama_key
import streamlit as st
from groq import Groq
import pandas as pd
import json


client = Groq(
    api_key=(llama_key))
with open("json_file.json", "r") as f:
    data = json.load(f)
st.title('Financial Assistant')


input_text = st.text_input("Search the topic: ")

response = client.chat.completions.create(
    
        messages=[
    {"role": "system", "content": f"You are a helpful financial assistant. Given the dataset {data} answer the queries with data from the dataset . Also give some financial advise"},
    {"role": "user", "content": input_text}
    
        ],
    model="llama3-8b-8192",
)
if input_text:

    
    st.write(response.choices[0].message.content)

