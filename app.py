import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="HealthWise", layout="wide")

# Load and encode images
logo_path = "pictures/logo.jpg"
hero_image_path = "pictures/fp.jpg"
feature_image_path = (
    "pictures/predict.png"  # Replace with actual image path for the feature card
)


def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()


# Encode images
encoded_logo = get_base64_image(logo_path)
encoded_hero_image = get_base64_image(hero_image_path)
encoded_feature_image = get_base64_image(feature_image_path)

# --- Navigation Bar ---
navbar_html = f"""
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
    }}
    .search-bar {{
        padding: 8px;
        font-size: 16px;
        border: 1px solid #ccc;
        border-radius: 15px;
        width: 250px;
        outline: none;
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
        <a href="#Contact">Contact</a>
        <input type="text" class="search-bar" placeholder="Search...">
    </div>
</div>
"""

# --- Hero Section ---
hero_section_html = f"""
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
"""

# --- Explore Our Features Section ---
features_section_html = """
<style>
    .features-section {
        padding: 60px;
        text-align: center;
        background-color: white;
        font-family: 'Poppins', sans-serif;
    }
    .features-heading {
        font-size: 40px;
        font-weight: bold;
        font-style: italic;
        color: #000000;
        margin-bottom: 20px;
    }
</style>
<div class="features-section">
    <div class="features-heading">Explore Our Features</div>
</div>
"""

# --- Feature Cards ---
# Feature card 1
feature_card_html1 = f"""
<style>
    .feature-card {{
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 20px auto;
        width: 80%;
        max-width: 800px;
    }}

    .feature-card img {{
        width: 40%;
        border-radius: 10px;
        margin-right: 20px;
    }}

    .feature-card-content {{
        flex: 1;
        text-align: left;
    }}

    .feature-card h3 {{
        font-size: 22px;
        color: #404040;
        margin-bottom: 10px;
    }}

    .feature-card p {{
        font-size: 16px;
        color: #555;
        margin-bottom: 15px;
    }}

    .feature-card button {{
        background-color: #007bff;
        color: white;
        padding: 10px 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }}

    .feature-card button:hover {{
        background-color: #0056b3;
    }}
</style>
<div class="feature-card">
    <img src="data:image/jpeg;base64,{encoded_feature_image}" alt="Feature Image">
    <div class="feature-card-content">
        <h3>Disease Prediction</h3>
        <p>Estimate the likelihood of developing a specific disease based on your symptoms and health history. Gain insights to manage health risks proactively.</p>
        <a href="pages/diseaseprediction.py" target="_blank">
    <button>Try Now</button>
</a>
</div>
"""

# Feature card 2
feature_card_html2 = f"""
<style>
    .feature-card {{
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 20px auto;
        width: 80%;
        max-width: 800px;
    }}

    .feature-card img {{
        width: 40%;
        border-radius: 10px;
        margin-right: 20px;
    }}

    .feature-card-content {{
        flex: 1;
        text-align: left;
    }}

    .feature-card h3 {{
        font-size: 22px;
        color: #404040;
        margin-bottom: 10px;
    }}

    .feature-card p {{
        font-size: 16px;
        color: #555;
        margin-bottom: 15px;
    }}

    .feature-card button {{
        background-color: #007bff;
        color: white;
        padding: 10px 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }}

    .feature-card button:hover {{
        background-color: #0056b3;
    }}
</style>
<div class="feature-card">
    <img src="data:image/jpeg;base64,{encoded_feature_image}" alt="Feature Image">
    <div class="feature-card-content">
        <h3>Precautionary Measures</h3>
        <p>Discover essential precautions and preventive measures to safeguard against potential health threats.</p>
        <a href="pages/precautions.py" target="_blank">
    <button>See</button>
</a>
</div>
"""

# Feature card 3
feature_card_html3 = f"""
<style>
    .feature-card {{
        display: flex;
        align-items: center;
        justify-content: center;
        background-color: #ffffff;
        border: 1px solid #ddd;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        padding: 20px;
        margin: 20px auto;
        width: 80%;
        max-width: 800px;
    }}

    .feature-card img {{
        width: 40%;
        border-radius: 10px;
        margin-right: 20px;
    }}

    .feature-card-content {{
        flex: 1;
        text-align: left;
    }}

    .feature-card h3 {{
        font-size: 22px;
        color: #404040;
        margin-bottom: 10px;
    }}

    .feature-card p {{
        font-size: 16px;
        color: #555;
        margin-bottom: 15px;
    }}

    .feature-card button {{
        background-color: #007bff;
        color: white;
        padding: 10px 16px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        transition: background-color 0.3s;
    }}

    .feature-card button:hover {{
        background-color: #0056b3;
    }}
</style>
<div class="feature-card">
    <img src="data:image/jpeg;base64,{encoded_feature_image}" alt="Feature Image">
    <div class="feature-card-content">
        <h3>Disease Information</h3>
        <p>Access comprehensive descriptions of various diseases, including their causes, symptoms, and treatment options.</p>
        <a href="pages/precautions.py" target="_blank">
    <button>See</button>
</a>
</div>
"""


# --- Render Components ---
st.markdown(navbar_html, unsafe_allow_html=True)
st.markdown(hero_section_html, unsafe_allow_html=True)
st.markdown(features_section_html, unsafe_allow_html=True)
st.markdown(feature_card_html1, unsafe_allow_html=True)
st.markdown(feature_card_html2, unsafe_allow_html=True)
st.markdown(feature_card_html3, unsafe_allow_html=True)


