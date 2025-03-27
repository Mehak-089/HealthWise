import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="HealthWise", layout="wide")

# Load and encode the logo image (Replace 'logo.jpg' with the correct path)
logo_path = "logo.jpg"  

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Encode the image
encoded_logo = get_base64_image(logo_path)

# Create a navigation bar using HTML and CSS
navbar_html = f"""
<style>
    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: white;
        padding: 10px 20px;
        border-bottom: 2px solid #ddd;
    }}
    .navbar .left-section {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}
    .navbar .app-name {{
        font-size: 20px;
        font-weight: bold;
        color: black;
    }}
    .navbar .nav-links {{
        display: flex;
        gap: 20px;
    }}
    .navbar .nav-links a {{
        text-decoration: none;
        color: black;
        font-size: 16px;
        font-weight: bold;
    }}
    .navbar .nav-links a:hover {{
        text-decoration: underline;
    }}
    .navbar img {{
        height: 40px;
        width: 40px;
    }}
</style>
<div class="navbar">
    <div class="left-section">
        <img src="data:image/jpeg;base64,{encoded_logo}" alt="Logo">
        <div class="app-name">HealthWise</div>
    </div>
    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#about">About</a>
    </div>
</div>
"""

# Render the navigation bar
st.markdown(navbar_html, unsafe_allow_html=True)
