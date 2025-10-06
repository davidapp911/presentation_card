from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "selfie.jpeg"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "David Parra's profile"
PAGE_ICON = ":wave:"
NAME = "David Parra"
DESCRIPTION = """
QA Automation trainee
"""
EMAIL = "davidapp91@gmail.com / david_parra@epam.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://linkedin.com/in/david-abdiel-parra-pena",
    "GitHub":"https://github.com/davidapp911",
}
PROFILE_INFO = {
    "Current training program (Primary Skill)":"Automated Testing in Python",
    "Complementary skills":"Python development, Web Dev, Data analysis and visualization",
    "Alternative career paths":"Full-Stack Development, Data Analysis",
    "Growth motivations":"Passion for continuous learning, interest in AI and Cloud/DevOps, driven to build impactful and innovative systems",
    "Current status of your training":"COMPLETED",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# --- Profile Info ---
st.markdown("""---------""")
st.subheader("Profile Info")
st.markdown("""---------""")
for question, answer in PROFILE_INFO.items():
    st.markdown(
        f"""
        <p><u>{question} :</u> {answer}</p>
        """,
        unsafe_allow_html=True
    )