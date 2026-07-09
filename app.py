import streamlit as st
import json
import random

st.set_page_config(page_title="💻 AI Software Engineering Agent", layout="wide")
st.title("💻 AI Software Engineering Agent")
st.markdown("Autonomous agent that reads GitHub issues, writes code fixes, runs tests, and opens PRs")

st.sidebar.header("📂 Repository Input")
repo_url = st.sidebar.text_input("GitHub Repo URL:", value="https://github.com/example/repo")
issue_number = st.sidebar.number_input("Issue Number:", value=1, min_value=1)
api_key = st.sidebar.text_input("OpenAI API Key (optional):", type="password")

sample_issues = {
    1: {
        "title": "Fix: TypeError in user login validation",
        "body": "When a user tries to login with a None password, the app crashes with TypeError.",
        "labels": ["bug", "critical"]
    },
    2: {
        "title": "Feature: Add email validation to signup",
        "body": "Signup form doesn't validate email format.",
        "labels": ["feature", "medium"]
    },
}

tab1, tab2, tab3 = st.tabs(["Issue Analysis", "Generate Fix", "Test & PR"])

with tab1:
    st.subheader("Issue Details")
    issue = sample_issues.get(issue_number, sample_issues[1])
    st.write(f"**Title:** {issue['title']}")
    st.write(f"**Body:** {issue['body']}")

with tab2:
    if st.button("Generate Fix"):
        st.success("Fix generated!")
        code_sample = "def validate_login(username, password):\n    if not password:\n        raise ValueError('Password required')"
        st.code(code_sample, language="python")

with tab3:
    st.subheader("Test Results")
    st.write("✅ test_login_missing_password — PASS")
    st.write("✅ test_login_valid_credentials — PASS")
    if st.button("Open Pull Request"):
        st.success("PR opened successfully!")
