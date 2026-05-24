import streamlit as st

st.title("AI Resume Scanner & Job Ranker")

# Input
resume = st.text_area("Paste Your Resume")
job = st.text_area("Paste Job Description")

def analyze(resume, job):
    resume_set = set(resume.lower().split())
    job_set = set(job.lower().split())

    matched = resume_set.intersection(job_set)
    missing = job_set - resume_set

    if len(job_set) == 0:
        return 0, set(), set()

    score = (len(matched) / len(job_set)) * 100
    return score, matched, missing


if st.button("Analyze"):
    score, matched, missing = analyze(resume, job)

    st.subheader("Match Score")
    st.write(round(score, 2), "%")

    st.subheader("Matched Skills")
    st.write(matched)

    st.subheader("Missing Skills")
    st.write(missing)

    # Simple ranking logic
    if score > 60:
        st.success("Strong Match - Apply Recommended")
    elif score > 30:
        st.warning("Moderate Match - Review before applying")
    else:
        st.error("Weak Match - Not Recommended")
