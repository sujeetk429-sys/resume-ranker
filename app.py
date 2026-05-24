import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("AIzaSyAOkTN4rEMtiWN0ivYlfyqMDEjvlOb5rV8"))

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI Resume Scanner", layout="centered")

st.title("🧠 AI Resume Scanner & Job Ranker")

st.markdown("Paste your resume and job description to get AI-powered insights.")

resume = st.text_area("📄 Paste Resume", height=200)
job = st.text_area("💼 Paste Job Description", height=200)

def get_ai_analysis(resume, job):
    prompt = f"""
    You are an expert HR assistant.

    Compare this resume and job description:

    RESUME:
    {resume}

    JOB DESCRIPTION:
    {job}

    Provide:
    1. Match score out of 100
    2. Matched skills
    3. Missing skills
    4. Final recommendation (Hire / Maybe / Reject)
    5. Short explanation
    """

    response = model.generate_content(prompt)
    return response.text


if st.button("🚀 Analyze"):
    if resume and job:
        with st.spinner("AI is analyzing..."):
            result = get_ai_analysis(resume, job)

        st.success("Analysis Complete")

        st.markdown("### 📊 AI Result")
        st.write(result)
    else:
        st.error("Please enter both resume and job description")
