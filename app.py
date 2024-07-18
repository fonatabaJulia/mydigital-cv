

from pathlib import Path

import streamlit as st
from PIL import Image, ImageFilter
import io

#------ PATH SETTINGS -----

#menggunakan parent atribut untuk 
current_dir  =  Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "style" / "main.css"
resume_file = current_dir / "assets" / "CV_jfonataba.pdf"
profile_pict = current_dir / "assets" / "profile-pic.png"
profile_pict2 = current_dir / "assets" / "profile-pic2.png"

img = Image.open(profile_pict)

# img = img.filter(ImageFilter.BLUR)
# img = img.filter(ImageFilter.GaussianBlur(radius=10))

# # Resize the image to the desired width
# img = img.resize((200, 200), Image.NEAREST)

# # Convert the image to bytes
# img_byte = io.BytesIO()
# img.save(img_byte, format='PNG')
# img_byte.seek(0)

#------ GENERAL SETTINGS --------
PAGE_TITLE = "DIGITAL CV | Julia Theresia Fonataba"
PAGE_ICON = "random"
NAME = "Julia Theresia Fonataba"
DESCRIPTION = """Hi, im jules an Computer Engineering student who loves to do Data Analysis"""
EMAIL = "juliatheresiafonataba@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/julia-theresia-fonataba-763a152a0/",
    "Github" : "https://github.com/fonatabaJulia",
    "Instagram" : "https://www.instagram.com/fonataba_julia/",

}

# PROJECTS = {
#     "🏆 Final Project Deep Learning, Using Long-Short Term Memory and Gated Reccurent Unit To Predict Air Quality in Jakarta (Grade: B+)",
#     "🏆 Embedded System Design & Internet of Things Developing Tools to Remotely Monitor Water Quality in Real-Time",
#     "🏆 ACES Leaguage(Programming Competencies) :  Runner up",
#     "🏆 Twitter Sentiment Analysis using Logistic Regression",

# }

PROJECTS = {
    "🏆 Final Project Deep Learning, Using Long-Short Term Memory and Gated Reccurent Unit To Predict Air Quality in Jakarta (Grade: B+)",
    "🏆 Embedded System Design & Internet of Things Developing Tools to Remotely Monitor Water Quality in Real-Time",
    "🏆 ACES Leaguage(Programming Competencies) :  Runner up",
    "🏆 Twitter Sentiment Analysis using Logistic Regression",
}

# for project in PROJECTS:
#     st.write(f"[{project}]")

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

st.title("Hello There!")


#------load untuk CSS, PDF, dan Profile Picture
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte =  pdf_file.read()
    profile_pict = Image.open(profile_pict)
    



#------- HERO SECTION ------
col1, col2 = st.columns(2, gap="small")
with col1: 
    st.image(profile_pict, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=str(resume_file),
        mime="aplication/octet-stream",
    )
    st.write("📫", EMAIL)
    




    #--------SOCIAL LINKS --------
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

    
    #-------PENGALAMAN -------
st.write('\n')
st.subheader("Experience: Organization")
st.write("---")
st.write(
        """
        ✔️ Association of Computer Engineering Student (ACES) -  As the Secretary and Tresurer

        ✔️ ACES - As a member of Public Relations Team

        ✔️ Pengenalan Prodi Teknik Komputer - As a member of Documentation Team
        
        ✔️ GEAR - As a member of LO & Registration Team
        """
    )



    #------------ SKILLS ----------

st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python, C language, PHP
- 📊 Data Visulization: Tableau, PowerBI
- 📚 Modeling: Logistic regression, Long-Short Term Memory, Gated Reccurent Unit
- 🗄️ Databases: MySQL  

"""
    )


#----- WORK HISTORY --------
st.write('\n')
st.subheader('Work History')
st.write("------")

#-----Job 1 
st.write("🚧", "Internship as Data Analyst |  PT. Freeport Indonesia")
st.write("06/2024 -  Present")
st.write(
     """
<link rel="stylesheet" type="text/css" href="main.css">
""",
    unsafe_allow_html=True
)
st.write(
    """
- ► As an Internship in Department MIS - division Ops.Infranstructur Process Controll Network (PCN)
- ► Used Google Collab and Python to Analysis Data for my Project
""",

    unsafe_allow_html=True
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
# for project, link in PROJECTS.items():
#     st.write(f"[{project}]({link})")
for project in PROJECTS:
        st.write(f"{project}")
