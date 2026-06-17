import streamlit as st
from config import GITHUB_PROJECTS, SOCIAL_MEDIA, ICONS

def render_projects():
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
        <div class="project-category">{{p['category']}}</div>
        <div class="project-title">{{p['name']}}</div>
        <div class="project-desc">{{p['description']}}</div>
        <div class="project-tags">
            {"".join(f'<span class="project-tag">#{t}</span>' for t in p["topics"])}
        </div>
    </div>
    <div class="project-footer">
        <span class="project-language">
            {{p['language']}}
        </span>
        <a href="{{p['url']}}" target="_blank" class="project-btn">View Code ↗</a>
    </div>
</div>
                    """,
                    unsafe_allow_html=True,
                )
