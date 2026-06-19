import streamlit as st
import textwrap
from config import EMAIL, SOCIAL_MEDIA, ICONS

def render_about():
    st.markdown(textwrap.dedent(f"""
<div class="project-card" style="min-height: auto; padding: 40px; margin-top: 20px; text-align: center;">
    <h1 style="color: var(--primary-color); margin-bottom: 25px; font-weight: 800; font-size: 2.5em; display:flex; justify-content:center; align-items:center;">{ICONS['user']}Hi, I'm Blina!</h1>
    <p style="font-size: 1.15em; color: var(--text-color); opacity: 0.9; line-height: 1.8; margin-bottom: 35px; max-width: 800px; margin-left: auto; margin-right: auto;">
        I am a Software & AI Engineer passionate about building intelligent systems
        and full-stack applications. With experience in computer vision, machine learning,
        and backend development, I combine strong technical skills with a drive to
        deliver impactful solutions.
    </p>
    <div style="display: flex; gap: 15px; align-items: center; justify-content: center; flex-wrap: wrap;">
        <a href="mailto:{EMAIL}" class="project-btn" style="text-decoration: none; padding: 10px 24px; font-size: 1em; display:flex; align-items:center;">{ICONS['mail']}Email Me</a>
        <a href="{SOCIAL_MEDIA['LinkedIn']}" target="_blank" class="project-btn" style="text-decoration: none; padding: 10px 24px; font-size: 1em; display:flex; align-items:center;">{ICONS['linkedin']}LinkedIn</a>
        <a href="{SOCIAL_MEDIA['GitHub']}" target="_blank" class="project-btn" style="text-decoration: none; padding: 10px 24px; font-size: 1em; display:flex; align-items:center;">{ICONS['github']}GitHub</a>
    </div>
</div>
    """), unsafe_allow_html=True)
