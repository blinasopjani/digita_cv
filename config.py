import streamlit as st

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

ICONS = {
    "mail": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path><polyline points="22,6 12,13 2,6"></polyline></svg>',
    "briefcase": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"></rect><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"></path></svg>',
    "code": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>',
    "book": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>',
    "grid": '<svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 12px;"><rect x="3" y="3" width="7" height="7"></rect><rect x="14" y="3" width="7" height="7"></rect><rect x="14" y="14" width="7" height="7"></rect><rect x="3" y="14" width="7" height="7"></rect></svg>',
    "github": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>',
    "linkedin": '<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 6px;"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>',
    "award": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><circle cx="12" cy="8" r="7"></circle><polyline points="8.21 13.89 7 23 12 20 17 23 15.79 13.88"></polyline></svg>',
    "user": '<svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 12px;"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"></path><circle cx="12" cy="7" r="4"></circle></svg>',
    "book-open": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path></svg>',
    "database": '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="vertical-align: middle; margin-right: 8px;"><ellipse cx="12" cy="5" rx="9" ry="3"></ellipse><path d="M21 12c0 1.66-4 3-9 3s-9-1.34-9-3"></path><path d="M3 5v14c0 1.66 4 3 9 3s9-1.34 9-3V5"></path></svg>'
}

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
