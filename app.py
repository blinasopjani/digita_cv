import streamlit as st
from PIL import Image

# Import configuration
from config import PAGE_TITLE, PAGE_ICON

# Set page config at the very beginning
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Load CSS from external file globally
with open("styles/main.css", encoding="utf-8") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Import views
from views.home import render_home
from views.about import render_about
from views.projects import render_projects
from views.lessons import render_lessons

# Pre-load assets
resume_file = "assets/egezon_cv_12_2024.pdf"
profile_pic_file = "assets/profile-pic.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About", "Projects", "Lessons"])

if page == "Home":
    render_home(profile_pic, PDFbyte)
elif page == "About":
    render_about()
elif page == "Projects":
    render_projects()
elif page == "Lessons":
    render_lessons()
