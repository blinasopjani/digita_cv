import streamlit as st
from config import NAME, DESCRIPTION, EMAIL, SOCIAL_MEDIA, ICONS

def render_home(profile_pic, PDFbyte):
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
        <h3 style="color: var(--primary-color); margin-bottom: 15px; font-weight: 700;">{ICONS['award']}Experience & Qualifications</h3>
        <ul style="color: var(--text-color); opacity: 0.9; line-height: 1.8; font-size: 1.05em; padding-left: 20px; margin-bottom: 0;">
            <li>Solid academic and practical background in Computer Science, Big Data, and AI.</li>
            <li>Experience in developing computer vision systems (YOLO) and ML models (Random Forest, SVM).</li>
            <li>Proficient in backend architecture using Java (Spring Boot) and Python.</li>
            <li>Experienced in building predictive pipelines, data automation, and dashboard visualization.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- SKILLS ---
    st.markdown(f"""
    <h3 style="color: var(--text-color); margin-top: 40px; margin-bottom: 20px; font-weight: 700;">{ICONS['code']}Hard Skills</h3>
    """, unsafe_allow_html=True)

    col_skill1, col_skill2 = st.columns(2)
    with col_skill1:
        st.markdown("""
        <div class="project-card skill-card" style="min-height: 200px; padding: 24px; margin-bottom: 20px;">
            <div style="font-size: 1.15em; font-weight: bold; color: var(--primary-color); margin-bottom: 15px;">Programming</div>
            <div class="project-tags">
                <span class="project-tag">Python</span>
                <span class="project-tag">Java (Spring Boot)</span>
                <span class="project-tag">C# .NET</span>
                <span class="project-tag">JavaScript</span>
                <span class="project-tag">React Native</span>
            </div>
        </div>
        
        <div class="project-card skill-card" style="min-height: 200px; padding: 24px; margin-bottom: 20px;">
            <div style="font-size: 1.15em; font-weight: bold; color: var(--primary-color); margin-bottom: 15px;">Databases & Tools</div>
            <div class="project-tags">
                <span class="project-tag">PostgreSQL</span>
                <span class="project-tag">MySQL</span>
                <span class="project-tag">MongoDB</span>
                <span class="project-tag">Git</span>
                <span class="project-tag">Docker</span>
                <span class="project-tag">Linux</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_skill2:
        st.markdown("""
        <div class="project-card skill-card" style="min-height: 200px; padding: 24px; margin-bottom: 20px;">
            <div style="font-size: 1.15em; font-weight: bold; color: var(--primary-color); margin-bottom: 15px;">Machine Learning & AI</div>
            <div class="project-tags">
                <span class="project-tag">Computer Vision</span>
                <span class="project-tag">YOLO</span>
                <span class="project-tag">OpenCV</span>
                <span class="project-tag">NLP</span>
                <span class="project-tag">Scikit-learn</span>
            </div>
        </div>
        
        <div class="project-card skill-card" style="min-height: 200px; padding: 24px; margin-bottom: 20px;">
            <div style="font-size: 1.15em; font-weight: bold; color: var(--primary-color); margin-bottom: 15px;">Data Visualization</div>
            <div class="project-tags">
                <span class="project-tag">Power BI</span>
                <span class="project-tag">Tableau</span>
                <span class="project-tag">Matplotlib</span>
                <span class="project-tag">Seaborn</span>
                <span class="project-tag">Plotly</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # --- WORK HISTORY ---
    st.markdown(f"""
    <h3 style="color: var(--text-color); margin-top: 40px; margin-bottom: 20px; font-weight: 700;">{ICONS['briefcase']}Work History</h3>
    
    <div class="project-card" style="min-height: auto; padding: 20px 24px; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
            <div>
                <div style="font-size: 1.15em; font-weight: bold; color: var(--text-color);">Project Manager</div>
                <div style="color: var(--primary-color); font-weight: 600; margin-top: 4px;">Siqa Store, Remote</div>
            </div>
            <div style="background: rgba(255, 77, 141, 0.1); color: var(--primary-color); padding: 4px 14px; border-radius: 12px; font-size: 0.85em; font-weight: bold; border: 1px solid rgba(255, 77, 141, 0.2);">
                01/2025 - Present
            </div>
        </div>
        <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em;">
            <li>Managing project lifecycles and coordinating remote team operations.</li>
            <li>Leading strategic planning and project execution processes.</li>
        </ul>
    </div>

    <div class="project-card" style="min-height: auto; padding: 20px 24px; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
            <div>
                <div style="font-size: 1.15em; font-weight: bold; color: var(--text-color);">Python & Data Science Intern</div>
                <div style="color: var(--primary-color); font-weight: 600; margin-top: 4px;">Tectigon LLC, Pristina</div>
            </div>
            <div style="background: rgba(255, 77, 141, 0.1); color: var(--primary-color); padding: 4px 14px; border-radius: 12px; font-size: 0.85em; font-weight: bold; border: 1px solid rgba(255, 77, 141, 0.2);">
                02/2026 - 04/2026
            </div>
        </div>
        <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em;">
            <li>Automated data extraction workflows and built predictive ML models for trend forecasting.</li>
            <li>Designed executive reports and interactive dashboards using Power BI.</li>
        </ul>
    </div>

    <div class="project-card" style="min-height: auto; padding: 20px 24px; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
            <div>
                <div style="font-size: 1.15em; font-weight: bold; color: var(--text-color);">AI Developer Intern</div>
                <div style="color: var(--primary-color); font-weight: 600; margin-top: 4px;">KPN Telecom, Netherlands</div>
            </div>
            <div style="background: rgba(255, 77, 141, 0.1); color: var(--primary-color); padding: 4px 14px; border-radius: 12px; font-size: 0.85em; font-weight: bold; border: 1px solid rgba(255, 77, 141, 0.2);">
                01/2025 - 06/2025
            </div>
        </div>
        <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em;">
            <li>Developed an automated FTU installation validation system using YOLO object detection.</li>
            <li>Significantly reduced manual hardware inspection overhead.</li>
        </ul>
    </div>

    <div class="project-card" style="min-height: auto; padding: 20px 24px; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
            <div>
                <div style="font-size: 1.15em; font-weight: bold; color: var(--text-color);">IT Instructor</div>
                <div style="color: var(--primary-color); font-weight: 600; margin-top: 4px;">NdreqiNotat.com, Pristina</div>
            </div>
            <div style="background: rgba(255, 77, 141, 0.1); color: var(--primary-color); padding: 4px 14px; border-radius: 12px; font-size: 0.85em; font-weight: bold; border: 1px solid rgba(255, 77, 141, 0.2);">
                09/2024 - 09/2025
            </div>
        </div>
        <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em;">
            <li>Taught programming fundamentals, algorithms, and logical problem-solving.</li>
            <li>Reinforced clean coding practices across student cohorts.</li>
        </ul>
    </div>

    <div class="project-card" style="min-height: auto; padding: 20px 24px; margin-bottom: 15px; border-left: 5px solid var(--primary-color);">
        <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px; flex-wrap: wrap; gap: 10px;">
            <div>
                <div style="font-size: 1.15em; font-weight: bold; color: var(--text-color);">Java & Web Developer Intern</div>
                <div style="color: var(--primary-color); font-weight: 600; margin-top: 4px;">Sharp Group LTD, Pristina</div>
            </div>
            <div style="background: rgba(255, 77, 141, 0.1); color: var(--primary-color); padding: 4px 14px; border-radius: 12px; font-size: 0.85em; font-weight: bold; border: 1px solid rgba(255, 77, 141, 0.2);">
                10/2023 - 11/2023
            </div>
        </div>
        <ul style="color: var(--text-color); opacity: 0.85; margin: 0; padding-left: 20px; line-height: 1.6; font-size: 0.95em;">
            <li>Built backend Java applications and web interfaces.</li>
            <li>Integrated frontend HTML/JS with database endpoints for client projects.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # --- EDUCATION ---
    st.markdown(f"""
    <h3 style="color: var(--text-color); margin-top: 40px; margin-bottom: 20px; font-weight: 700;">{ICONS['book']}Education</h3>
    <div class="project-card" style="min-height: auto; padding: 24px; display: flex; flex-direction: column; gap: 20px;">
        <div style="display: flex; align-items: center; gap: 20px;">
            <div>
                <div style="font-size: 1.15em; font-weight: bold; color: var(--text-color);">BSc in Computer Science</div>
                <div style="color: var(--text-color); opacity: 0.7; margin-top: 4px;">Universum International College, Pristina</div>
            </div>
        </div>
        <div style="border-top: 1px solid rgba(128,128,128,0.2); padding-top: 20px; display: flex; align-items: center; gap: 20px;">
            <div>
                <div style="font-size: 1.15em; font-weight: bold; color: var(--text-color);">Erasmus Exchange (Big Data & AI)</div>
                <div style="color: var(--text-color); opacity: 0.7; margin-top: 4px;">Inholland University of Applied Sciences, Netherlands</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
