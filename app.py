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

# --- GITHUB PROJECTS DATA ---
GITHUB_PROJECTS = [
    {
        "name": "Personal Portfolio",
        "repo": "Personal-Portfolio",
        "description": "Modern personal portfolio website showcasing skills, projects, and experience as a Software & AI Engineer.",
        "language": "HTML",
        "lang_color": "#e34c26",
        "topics": ["portfolio", "web", "html"],
        "url": "https://github.com/blinasopjani/Personal-Portfolio",
        "icon": "🌐",
        "category": "Web Development",
    },
    {
        "name": "RSNA Brain Aneurysm Detection",
        "repo": "RSNA-Aneurysm",
        "description": "Deep learning pipeline for detecting brain aneurysms from medical imaging data using the RSNA dataset. Computer vision & AI-powered diagnostic tool.",
        "language": "Python",
        "lang_color": "#3572A5",
        "topics": ["deep-learning", "computer-vision", "medical-ai", "python"],
        "url": "https://github.com/blinasopjani/RSNA-Aneurysm",
        "icon": "🧠",
        "category": "AI & Machine Learning",
    },
    {
        "name": "EcoMind AI",
        "repo": "EcoMind-AI",
        "description": "AI-powered sustainability platform that helps users track their environmental impact and receive personalized eco-friendly recommendations.",
        "language": "JavaScript",
        "lang_color": "#f1e05a",
        "topics": ["ai", "sustainability", "javascript", "web-app"],
        "url": "https://github.com/blinasopjani/EcoMind-AI",
        "icon": "🌱",
        "category": "AI & Web Development",
    },
    {
        "name": "UniFLIX Movie API",
        "repo": "uniflix-movie-api",
        "description": "Secure enterprise-grade streaming backend built with Java Spring Boot. Features JWT authentication, RESTful API design, and PostgreSQL integration.",
        "language": "Java",
        "lang_color": "#b07219",
        "topics": ["spring-boot", "java", "rest-api", "backend", "jwt"],
        "url": "https://github.com/blinasopjani/uniflix-movie-api",
        "icon": "🎬",
        "category": "Backend Development",
    },
    {
        "name": "Student Dropout Prediction",
        "repo": "Student-Dropout-Prediction",
        "description": "Machine learning API using Random Forest classifier to predict student dropout risk based on academic and socioeconomic features.",
        "language": "Jupyter Notebook",
        "lang_color": "#DA5B0B",
        "topics": ["machine-learning", "random-forest", "data-science", "python"],
        "url": "https://github.com/blinasopjani/Student-Dropout-Prediction",
        "icon": "🎓",
        "category": "Data Science",
    },
    {
        "name": "Candy Sales Data Analysis",
        "repo": "Candy-Sales-Data-Analysis",
        "description": "Comprehensive exploratory data analysis and visualization of candy sales dataset. Includes trend analysis, forecasting, and interactive Power BI dashboards.",
        "language": "Jupyter Notebook",
        "lang_color": "#DA5B0B",
        "topics": ["data-analysis", "visualization", "pandas", "matplotlib"],
        "url": "https://github.com/blinasopjani/Candy-Sales-Data-Analysis",
        "icon": "📊",
        "category": "Data Science",
    },
    {
        "name": "RPS Hand Gesture Recognition",
        "repo": "rps-hand-gesture-recognition",
        "description": "Real-time Rock-Paper-Scissors game using computer vision and hand gesture recognition with OpenCV and MediaPipe.",
        "language": "Python",
        "lang_color": "#3572A5",
        "topics": ["computer-vision", "opencv", "mediapipe", "gesture-recognition"],
        "url": "https://github.com/blinasopjani/rps-hand-gesture-recognition",
        "icon": "✋",
        "category": "Computer Vision",
    },
    {
        "name": "Happiness Data Insights",
        "repo": "happiness-data-insights",
        "description": "Data analysis project exploring the World Happiness Report dataset to uncover patterns and correlations between happiness scores and socioeconomic indicators.",
        "language": "Jupyter Notebook",
        "lang_color": "#DA5B0B",
        "topics": ["data-science", "visualization", "world-happiness", "analytics"],
        "url": "https://github.com/blinasopjani/happiness-data-insights",
        "icon": "😊",
        "category": "Data Science",
    },
]

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# Directly reference files in the assets folder (ensure it exists)
resume_file = "assets/egezon_cv_12_2024.pdf"
profile_pic_file = "assets/profile-pic.png"

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

profile_pic = Image.open(profile_pic_file)

# Sidebar navigation
page = st.sidebar.radio("Navigate", ["Home", "Projects", "About"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="Blina_Sopjani_CV.pdf",
            mime="application/octet-stream",
        )
        st.write("📫", EMAIL)
        cols = st.columns(len(SOCIAL_MEDIA))
        for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
            cols[index].write(f"[{platform}]({link})")

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

elif page == "Projects":
    # --- PROJECTS PAGE ---
    st.title("🚀 My Projects")
    st.write("A collection of projects I've built and open-sourced on GitHub.")
    st.markdown(
        f"[View all repositories on GitHub →]({SOCIAL_MEDIA['GitHub']}?tab=repositories)"
    )
    st.write("---")

    # Category filter
    categories = sorted(set(p["category"] for p in GITHUB_PROJECTS))
    all_cats = ["All"] + categories
    selected_cat = st.selectbox("Filter by category:", all_cats)

    filtered = (
        GITHUB_PROJECTS
        if selected_cat == "All"
        else [p for p in GITHUB_PROJECTS if p["category"] == selected_cat]
    )

    st.write("")

    # Load CSS from external file
    with open("styles/main.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Render cards in 2-column grid
    LANG_ICON = {
        "Python": "🐍",
        "Java": "☕",
        "JavaScript": "⚡",
        "HTML": "🌐",
        "Jupyter Notebook": "📓",
    }

    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for col_idx, col in enumerate(cols):
            proj_idx = i + col_idx
            if proj_idx >= len(filtered):
                break
            p = filtered[proj_idx]
            lang_icon = LANG_ICON.get(p["language"], "💻")
            with col:
                st.markdown(
                    f"""
<div class="project-card">
    <div>
        <div class="project-icon">{p['icon']}</div>
        <div class="project-category">{p['category']}</div>
        <div class="project-title">{p['name']}</div>
        <div class="project-desc">{p['description']}</div>
        <div class="project-tags">
            {"".join(f'<span class="project-tag">#{t}</span>' for t in p["topics"])}
        </div>
    </div>
    <div class="project-footer">
        <span class="project-language">
            {lang_icon} {p['language']}
        </span>
        <a href="{p['url']}" target="_blank" class="project-btn">View Code ↗</a>
    </div>
</div>
                    """,
                    unsafe_allow_html=True,
                )

    st.write("")
    st.markdown("---")
    st.markdown(
        f"💡 *Shiko të gjitha projektet e mia në [GitHub]({SOCIAL_MEDIA['GitHub']}?tab=repositories)*"
    )

elif page == "About":
    st.title("About Me")
    st.write(f"""
    I am a Software & AI Engineer passionate about building intelligent systems
    and full-stack applications. With experience in computer vision, machine learning,
    and backend development, I combine strong technical skills with a drive to
    deliver impactful solutions.

    Feel free to reach out via email or connect on LinkedIn!
    """)
    st.write("📫", EMAIL)
    st.write(f"[LinkedIn]({SOCIAL_MEDIA['LinkedIn']}) | [GitHub]({SOCIAL_MEDIA['GitHub']})")

