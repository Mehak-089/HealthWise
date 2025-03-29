import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="HealthWise", layout="wide")

# Function to encode images in Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Load and encode images
logo_path = "pictures/logo.jpg"
hero_image_path = "pictures/fp.jpg"

encoded_logo = get_base64_image(logo_path)
encoded_hero_image = get_base64_image(hero_image_path)

# --- Navigation Bar ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: white;
        padding: 15px 30px;
        border-bottom: 2px solid #ddd;
        font-family: 'Poppins', sans-serif;
    }}
    .navbar .left-section {{
        display: flex;
        align-items: center;
        gap: 15px;
    }}
    .navbar .app-name {{
        font-size: 24px;
        font-weight: 600;
        color: #333;
        cursor: pointer;
        padding: 8px 15px;
        border-radius: 5px;
        transition: background-color 0.3s ease, color 0.3s ease;
    }}
    .navbar .app-name:hover {{
        background-color: #007bff;
        color: white;
    }}
    .navbar .nav-links {{
        display: flex;
        align-items: center;
        gap: 25px;
    }}
    .navbar .nav-links a {{
        text-decoration: none;
        color: #333;
        font-size: 18px;
        font-weight: 500;
        transition: color 0.3s ease;
    }}
    .navbar .nav-links a:hover {{
        color: #007bff;
    }}
    .navbar img {{
        height: 50px;
        width: 50px;
        border-radius: 50%;
    }}
    .search-bar {{
        padding: 8px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 15px;
        width: 250px;
        outline: none;
    }}
    .upper-heading {{
        text-align: left;
        font-size: 28px;
        font-weight: 600;
        color: #333;
        margin: 30px 0 10px 30px;
        font-family: 'Poppins', sans-serif;
        font-style: italic;
    }}
    .image-container {{
        text-align: center;
        margin-top: 10px;
    }}
    .image-container img {{
        width: 80%;
        max-width: 800px;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }}
</style>

<div class="navbar">
    <div class="left-section">
        <img src="data:image/jpeg;base64,{encoded_logo}" alt="Logo">
        <div class="app-name" onclick="location.reload()">HealthWise</div>
    </div>
    <div class="nav-links">
        <a href="#home">Home</a>
        <a href="#about">About</a>
        <a href="#contact">Contact</a>
        <input type="text" class="search-bar" placeholder="Search...">
    </div>
</div>
""", unsafe_allow_html=True)

# --- Hero Section ---
st.markdown(f"""
<style>
    .hero {{
        position: relative;
        width: 100%;
        height: 600px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        overflow: hidden;
        padding: 20px;
    }}
    
    .hero img {{
        width: 100%;
        height: 100%;
        object-fit: cover;
    }}
    .hero-text {{
        position: absolute;
        font-size: 50px;
        font-weight: bold;
        color: white;
        font-family: 'Arial';
        font-style: italic;
        text-shadow: 2px 2px 4px #000000;
    }}
    .hero-subtext {{
        position: absolute;
        top: 55%;
        font-size: 20px;
        font-weight: normal;
        color: white;
        font-family: 'Poppins', sans-serif;
        text-shadow: 1px 1px 3px #000000;
        max-width: 80%;
    }}
</style>
<div class="hero">
    <img src="data:image/jpeg;base64,{encoded_hero_image}" alt="Health Banner">
    <div class="hero-text">Exploring Your Health Journey</div>
    <div class="hero-subtext">
        Explore a wealth of information and tools to manage your well-being effectively. 
        From predicting potential health risks to understanding disease details, we've got you covered.
    </div>
</div>
""", unsafe_allow_html=True)
