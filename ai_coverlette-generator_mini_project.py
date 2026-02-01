import streamlit as st
import google.generativeai as genai

# Configure Gemini with your API key
genai.configure(api_key="AIzaSyAdTcpxXXADYiXNqR9GurkMcQXbqwiVsaY")
    
model = genai.GenerativeModel('gemini-2.5-flash')
    
# 1. AI Cover Letter Generator
job_title = st.text_input("Job Title")
resume_summary = st.text_area("Resume Summary")

if st.button("Generate Cover Letter"):
    prompt = f"Write a cover letter for {job_title} using these resume points:\n{resume_summary}"
    response = model.generate_content(prompt)
    st.write(response.text)
