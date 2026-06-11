import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Blina Sopjani"
PAGE_ICON = ":wave:"
NAME = "Blina Sopjani"
DESCRIPTION = """
Software & AI Engineer | AI Automation Engineer & Full-Stack Developer.
"""
EMAIL = "blina.sopjani@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/blina-sopjani/",
    "GitHub": "https://github.com/blinasopjani",
}
PROJECTS = {
    "🏆 RSNA Brain Aneurysm Detection - Deep learning pipeline for aneurysm detection": "https://github.com/blinasopjani/RSNA-Aneurysm",
    "🏆 UniFLIX Streaming API - Secure Java Spring Boot enterprise backend": "https://github.com/blinasopjani/uniflix-movie-api",
    "🏆 Student Dropout Prediction API - Random Forest classifier for academic scoring": "https://github.com/blinasopjani/Student-Dropout-Prediction",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/egezon_cv_12_2024.pdf"
profile_pic_file = "assets/profile-pic.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write("\n")
st.subheader("Experience & Qualifications")
st.write(
    """
- ✔️ Solid academic and practical background in Computer Science, Big Data, and AI.
- ✔️ Experience in developing computer vision systems (YOLO) and ML models (Random Forest, SVM).
- ✔️ Proficient in backend architecture using Java (Spring Boot) and Python.
- ✔️ Experienced in building predictive pipelines, data automation, and dashboard visualization.
"""
)

# --- SKILLS ---
st.write("\n")
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, Java (Spring Boot), C# .NET, JavaScript, React Native
- 🤖 Machine Learning & AI: Computer Vision (YOLO, OpenCV), NLP, Scikit-learn
- 🗄️ Databases & Tools: PostgreSQL, Git
- 📊 Data Visualization: Power BI
"""
)

# --- WORK HISTORY ---
st.write("\n")
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Project Manager | Siqa Store, Remote**")
st.write("01/2025 - Present")
st.write(
    """
- ► Managing project lifecycles and coordinating remote team operations.
- ► Leading strategic planning and project execution processes.
"""
)

# --- JOB 2
st.write("\n")
st.write("🚧", "**Python & Data Science Intern | Tectigon LLC, Pristina**")
st.write("02/2026 - 04/2026")
st.write(
    """
- ► Automated data extraction workflows and built predictive ML models for trend forecasting.
- ► Designed executive reports and interactive dashboards using Power BI.
"""
)

# --- JOB 3
st.write("\n")
st.write("🚧", "**AI Developer Intern | KPN Telecom, Netherlands**")
st.write("01/2025 - 06/2025")
st.write(
    """
- ► Developed an automated FTU installation validation system using YOLO object detection.
- ► Significantly reduced manual hardware inspection overhead.
"""
)

# --- JOB 4
st.write("\n")
st.write("🚧", "**IT Instructor | NdreqiNotat.com, Pristina**")
st.write("09/2024 - 09/2025")
st.write(
    """
- ► Taught programming fundamentals, algorithms, and logical problem-solving.
- ► Reinforced clean coding practices across student cohorts.
"""
)

# --- JOB 5
st.write("\n")
st.write("🚧", "**Java & Web Developer Intern | Sharp Group LTD, Pristina**")
st.write("10/2023 - 11/2023")
st.write(
    """
- ► Built backend Java applications and web interfaces.
- ► Integrated frontend HTML/JS with database endpoints for client projects.
"""
)

# --- EDUCATION ---
st.write("\n")
st.subheader("Education")
st.write("---")
st.write("🎓", "**BSc in Computer Science** - Universum International College, Pristina")
st.write("🎓", "**Erasmus Exchange (Big Data & AI)** - Inholland University of Applied Sciences, Netherlands")

# --- PROJECTS & ACCOMPLISHMENTS ---
st.write("\n")
st.subheader("Projects & Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
