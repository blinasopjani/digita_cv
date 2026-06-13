import streamlit as st
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Blina Sopjani"
PAGE_ICON = ""
NAME = "Blina Sopjani"
DESCRIPTION = """
Software & AI Engineer | AI Automation Engineer & Full-Stack Developer.
"""
EMAIL = "blina.sopjani@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/blina-sopjani/",
    "GitHub": "https://github.com/blinasopjani",
}

# --- ICONS ---
ICONS = {
    "mail": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
    "briefcase": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>',
    "code": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
    "book": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>',
    "grid": '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 12px;"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>',
    "github": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>',
    "linkedin": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
    "award": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>',
    "user": '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 12px;"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>'
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
page = st.sidebar.radio("Navigate", ["Home", "About", "Projects"])

if page == "Home":
    # --- HERO SECTION ---
    col1, col2 = st.columns([1, 2], gap="small")
    with col1:
        st.image(profile_pic, width=230)
    with col2:
        st.title(NAME)
        st.write(DESCRIPTION)
        st.download_button(
            label="Download Resume",
            data=PDFbyte,
            file_name="Blina_Sopjani_CV.pdf",
            mime="application/octet-stream",
        )
        st.markdown(f"""
        <div style="display: flex; gap: 15px; align-items: center; flex-wrap: wrap; margin-top: 20px;">
            <a href="mailto:{EMAIL}" class="project-btn" style="text-decoration: none; padding: 8px 20px; font-size: 0.9em; display:flex; align-items:center;">{ICONS['mail']}Email</a>
            <a href="{SOCIAL_MEDIA['LinkedIn']}" target="_blank" class="project-btn" style="text-decoration: none; padding: 8px 20px; font-size: 0.9em; display:flex; align-items:center;">{ICONS['linkedin']}LinkedIn</a>
            <a href="{SOCIAL_MEDIA['GitHub']}" target="_blank" class="project-btn" style="text-decoration: none; padding: 8px 20px; font-size: 0.9em; display:flex; align-items:center;">{ICONS['github']}GitHub</a>
        </div>
        """, unsafe_allow_html=True)

    # --- EXPERIENCE & QUALIFICATIONS ---
    st.markdown(f"""
    <div class="project-card" style="min-height: auto; margin-top: 30px;">
        <div>
            <div class="project-category">Overview</div>
            <div class="project-title" style="display:flex; align-items:center;">{ICONS['award']}Experience & Qualifications</div>
            <ul style="color: var(--text-color); opacity: 0.9; line-height: 1.8; font-size: 1.05em; padding-left: 20px; margin-bottom: 15px;">
                <li>Solid academic and practical background in Computer Science, Big Data, and AI.</li>
                <li>Experience in developing computer vision systems (YOLO) and ML models (Random Forest, SVM).</li>
                <li>Proficient in backend architecture using Java (Spring Boot) and Python.</li>
                <li>Experienced in building predictive pipelines, data automation, and dashboard visualization.</li>
            </ul>
        </div>
        <div class="project-footer">
            <span class="project-language">Professional Summary</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- SKILLS ---
    st.markdown(f"""
    <h3 style="color: var(--text-color); margin-top: 40px; margin-bottom: 20px; font-weight: 700;">{ICONS['code']}Hard Skills</h3>
    """, unsafe_allow_html=True)

    col_skill1, col_skill2 = st.columns(2)
    with col_skill1:
        st.markdown("""
        <div class="project-card" style="min-height: 220px; margin-bottom: 20px;">
            <div>
                <div class="project-category">Hard Skill</div>
                <div class="project-title">Programming</div>
                <div class="project-tags">
                    <span class="project-tag">Python</span>
                    <span class="project-tag">Java (Spring Boot)</span>
                    <span class="project-tag">C# .NET</span>
                    <span class="project-tag">JavaScript</span>
                    <span class="project-tag">React Native</span>
                </div>
            </div>
            <div class="project-footer">
                <span class="project-language">5 Technologies</span>
            </div>
        </div>
        
        <div class="project-card" style="min-height: 220px; margin-bottom: 20px;">
            <div>
                <div class="project-category">Hard Skill</div>
                <div class="project-title">Databases & Tools</div>
                <div class="project-tags">
                    <span class="project-tag">PostgreSQL</span>
                    <span class="project-tag">Git</span>
                </div>
            </div>
            <div class="project-footer">
                <span class="project-language">2 Technologies</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_skill2:
        st.markdown("""
        <div class="project-card" style="min-height: 220px; margin-bottom: 20px;">
            <div>
                <div class="project-category">Hard Skill</div>
                <div class="project-title">Machine Learning & AI</div>
                <div class="project-tags">
                    <span class="project-tag">Computer Vision</span>
                    <span class="project-tag">YOLO</span>
                    <span class="project-tag">OpenCV</span>
                    <span class="project-tag">NLP</span>
                    <span class="project-tag">Scikit-learn</span>
                </div>
            </div>
            <div class="project-footer">
                <span class="project-language">5 Technologies</span>
            </div>
        </div>
        
        <div class="project-card" style="min-height: 220px; margin-bottom: 20px;">
            <div>
                <div class="project-category">Hard Skill</div>
                <div class="project-title">Data Visualization</div>
                <div class="project-tags">
                    <span class="project-tag">Power BI</span>
                </div>
            </div>
            <div class="project-footer">
                <span class="project-language">1 Technology</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- WORK HISTORY ---
    st.markdown(f"""
    <h3 style="color: var(--text-color); margin-top: 40px; margin-bottom: 20px; font-weight: 700; display:flex; align-items:center;">{ICONS['briefcase']}Work History</h3>
    
    <div class="project-card" style="min-height: auto; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div>
            <div class="project-category">Siqa Store, Remote</div>
            <div class="project-title">Project Manager</div>
            <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em; margin-bottom: 15px;">
                <li>Managing project lifecycles and coordinating remote team operations.</li>
                <li>Leading strategic planning and project execution processes.</li>
            </ul>
        </div>
        <div class="project-footer">
            <span class="project-language">01/2025 - Present</span>
        </div>
    </div>

    <div class="project-card" style="min-height: auto; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div>
            <div class="project-category">Tectigon LLC, Pristina</div>
            <div class="project-title">Python & Data Science Intern</div>
            <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em; margin-bottom: 15px;">
                <li>Automated data extraction workflows and built predictive ML models for trend forecasting.</li>
                <li>Designed executive reports and interactive dashboards using Power BI.</li>
            </ul>
        </div>
        <div class="project-footer">
            <span class="project-language">02/2026 - 04/2026</span>
        </div>
    </div>

    <div class="project-card" style="min-height: auto; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div>
            <div class="project-category">KPN Telecom, Netherlands</div>
            <div class="project-title">AI Developer Intern</div>
            <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em; margin-bottom: 15px;">
                <li>Developed an automated FTU installation validation system using YOLO object detection.</li>
                <li>Significantly reduced manual hardware inspection overhead.</li>
            </ul>
        </div>
        <div class="project-footer">
            <span class="project-language">01/2025 - 06/2025</span>
        </div>
    </div>

    <div class="project-card" style="min-height: auto; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div>
            <div class="project-category">NdreqiNotat.com, Pristina</div>
            <div class="project-title">IT Instructor</div>
            <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em; margin-bottom: 15px;">
                <li>Taught programming fundamentals, algorithms, and logical problem-solving.</li>
                <li>Reinforced clean coding practices across student cohorts.</li>
            </ul>
        </div>
        <div class="project-footer">
            <span class="project-language">09/2024 - 09/2025</span>
        </div>
    </div>

    <div class="project-card" style="min-height: auto; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div>
            <div class="project-category">Sharp Group LTD, Pristina</div>
            <div class="project-title">Java & Web Developer Intern</div>
            <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em; margin-bottom: 15px;">
                <li>Built backend Java applications and web interfaces.</li>
                <li>Integrated frontend HTML/JS with database endpoints for client projects.</li>
            </ul>
        </div>
        <div class="project-footer">
            <span class="project-language">10/2023 - 11/2023</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # --- EDUCATION ---
    st.markdown(f"""
    <h3 style="color: var(--text-color); margin-top: 40px; margin-bottom: 20px; font-weight: 700; display:flex; align-items:center;">{ICONS['book']}Education</h3>
    
    <div class="project-card" style="min-height: auto; margin-bottom: 15px;">
        <div>
            <div class="project-category">Degree</div>
            <div class="project-title">BSc in Computer Science</div>
            <div class="project-desc" style="margin-bottom: 15px;">Universum International College, Pristina</div>
        </div>
        <div class="project-footer">
            <span class="project-language">Completed</span>
        </div>
    </div>

    <div class="project-card" style="min-height: auto; margin-bottom: 15px;">
        <div>
            <div class="project-category">Exchange Program</div>
            <div class="project-title">Erasmus Exchange (Big Data & AI)</div>
            <div class="project-desc" style="margin-bottom: 15px;">Inholland University of Applied Sciences, Netherlands</div>
        </div>
        <div class="project-footer">
            <span class="project-language">Completed</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

elif page == "Projects":
    # --- PROJECTS PAGE ---
    st.markdown(f"<h1 style='display:flex; align-items:center;'>{ICONS['grid']}My Projects</h1>", unsafe_allow_html=True)
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
    for i in range(0, len(filtered), 2):
        cols = st.columns(2)
        for col_idx, col in enumerate(cols):
            proj_idx = i + col_idx
            if proj_idx >= len(filtered):
                break
            p = filtered[proj_idx]
            with col:
                st.markdown(
                    f"""
<div class="project-card">
    <div>
        <div class="project-category">{p['category']}</div>
        <div class="project-title">{p['name']}</div>
        <div class="project-desc">{p['description']}</div>
        <div class="project-tags">
            {"".join(f'<span class="project-tag">#{t}</span>' for t in p["topics"])}
        </div>
    </div>
    <div class="project-footer">
        <span class="project-language">
            {p['language']}
        </span>
        <a href="{p['url']}" target="_blank" class="project-btn">View Code ↗</a>
    </div>
</div>
                    """,
                    unsafe_allow_html=True,
                )



elif page == "About":
    st.markdown(f"""
    <div class="project-card" style="min-height: auto; padding: 40px; margin-top: 20px; text-align: center;">
        <h1 style="color: var(--primary-color); margin-bottom: 25px; font-weight: 800; font-size: 2.5em; display:flex; justify-content:center; align-items:center;">{ICONS['user']}Hi, I'm Blina!</h1>
        <p style="font-size: 1.15em; color: var(--text-color); opacity: 0.9; line-height: 1.8; margin-bottom: 35px; max-width: 800px; margin-left: auto; margin-right: auto;">
            I am a Software & AI Engineer passionate about building intelligent systems
            and full-stack applications. With experience in computer vision, machine learning,
            and backend development, I combine strong technical skills with a drive to
            deliver impactful solutions.
        </p>
        <div style="display: flex; gap: 15px; align-items: center; justify-content: center; flex-wrap: wrap;">
            <a href="mailto:{{EMAIL}}" class="project-btn" style="text-decoration: none; padding: 10px 24px; font-size: 1em; display:flex; align-items:center;">{ICONS['mail']}Email Me</a>
            <a href="{{SOCIAL_MEDIA['LinkedIn']}}" target="_blank" class="project-btn" style="text-decoration: none; padding: 10px 24px; font-size: 1em; display:flex; align-items:center;">{ICONS['linkedin']}LinkedIn</a>
            <a href="{{SOCIAL_MEDIA['GitHub']}}" target="_blank" class="project-btn" style="text-decoration: none; padding: 10px 24px; font-size: 1em; display:flex; align-items:center;">{ICONS['github']}GitHub</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

