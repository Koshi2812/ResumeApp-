import streamlit as st
from fpdf import FPDF
from io import BytesIO

# ---- Set Page Config ----
st.set_page_config(page_title="📝 Resume Maker", layout="centered")

# ---- Add Background Image via CSS ----
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://th.bing.com/th/id/OSK.HERO4NfDOMnJhdNRrdXVxiqy1R_M2HIZPvmCibPuEu79xCM?o=7rm=3&rs=1&pid=ImgDetMain");
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("📝 Resume Maker with PDF Download")

# ===== User Inputs =====
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
summary = st.text_area("Professional Summary", height=100)

st.subheader("🎓 Education")
education = st.text_area("Enter your education details (e.g., B.Tech in CSE, XYZ University, 2020)")

st.subheader("💼 Experience")
experience = st.text_area("Enter your work experience (e.g., Software Intern at ABC Corp, 2022 - Present)")

st.subheader("💡 Skills")
skills = st.text_area("List your skills (e.g., Python, SQL, Streamlit)")

# ===== Generate PDF Function =====
def create_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=name, ln=True, align="C")

    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, txt=f"Email: {email} | Phone: {phone}", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Professional Summary", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, summary)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, education)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Experience", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, experience)

    pdf.ln(5)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", '', 12)
    pdf.multi_cell(0, 10, skills)

    return pdf

# ===== Generate & Download PDF =====
if st.button("📄 Generate Resume"):
    if name and email and phone:
        pdf = create_pdf()
        pdf_buffer = BytesIO()
        pdf_output = pdf.output(dest='S').encode('latin1')
        pdf_buffer.write(pdf_output)
        pdf_buffer.seek(0)

        st.success("✅ Resume generated successfully!")
        st.download_button(
            label="⬇️ Download Resume PDF",
            data=pdf_buffer,
            file_name=f"{name.replace(' ', '_')}_Resume.pdf",
            mime="application/pdf"
        )
    else:
        st.error("Please fill in at least Name, Email, and Phone.")
