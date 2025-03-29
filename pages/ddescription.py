import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="HealthWise", layout="wide")

# Function to encode images in Base64
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        return ""  # Return empty string if file is not found

# Image Paths
image_paths = {
    "logo": "pictures/logo.jpg",
    "hero": "pictures/fp.jpg",
    "varicose": "pictures/varicoseveins.jpg"
}

# Encoding images
encoded_images = {name: get_base64_image(path) for name, path in image_paths.items()}

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
        <img src="data:image/jpeg;base64,{encoded_images['logo']}" alt="Logo">
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
    <img src="data:image/jpeg;base64,{encoded_images['hero']}" alt="Health Banner">
    <div class="hero-text">Exploring Your Health Journey</div>
    <div class="hero-subtext">
        Explore a wealth of information and tools to manage your well-being effectively. 
        From predicting potential health risks to understanding disease details, we've got you covered.
    </div>
</div>
""", unsafe_allow_html=True)

# --- Flip Card Section ---
st.markdown(f'''
    <style>
        .flip-card {{
            background-color: transparent;
            width: 80%;
            max-width: 800px;
            height: 350px;
            perspective: 1000px;
            margin: 40px auto;
        }}

        .flip-card-inner {{
            position: relative;
            width: 100%;
            height: 100%;
            text-align: center;
            transition: transform 0.6s;
            transform-style: preserve-3d;
        }}

        .flip-card:hover .flip-card-inner {{
            transform: rotateY(180deg);
        }}

        .flip-card-front, .flip-card-back {{
            position: absolute;
            width: 100%;
            height: 100%;
            backface-visibility: hidden;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}

        .flip-card-front {{
            background-color: #ffffff;
            border: 1px solid #ddd;
            display: flex;
            align-items: center;
            padding: 20px;
        }}

        .flip-card-front img {{
            width: 40%;
            border-radius: 10px;
            margin-right: 20px;
            object-fit: cover;
            height: 100%;
        }}

        .flip-card-front-content {{
            flex: 1;
            text-align: left;
            padding: 10px;
        }}

        .flip-card-back {{
            background-color: #f8f9fa;
            transform: rotateY(180deg);
            padding: 20px;
            display: flex;
            flex-direction: column;
            justify-content: center;
        }}

        .flip-card h3 {{
            font-size: 22px;
            color: #404040;
            margin-bottom: 15px;
        }}

        .flip-card p {{
            font-size: 16px;
            color: #555;
            margin-bottom: 10px;
        }}

        .flip-card ul {{
            text-align: left;
            padding-left: 20px;
        }}

        .flip-card li {{
            margin-bottom: 8px;
        }}
    </style>

    <div class="flip-card">
        <div class="flip-card-inner">
            <div class="flip-card-front">
                <img src="data:image/jpeg;base64,{encoded_images['varicose']}" alt="Varicose Veins">
                <div class="flip-card-front-content">
                    <h3>Varicose Veins</h3>
                    <p>Varicose veins are enlarged, swollen, twisted veins that often appear blue or dark purple. They occur when faulty valves in the veins allow blood to flow in the wrong direction.</p>
                </div>
            </div>
            <div class="flip-card-back">
                <h3>Detailed Information</h3>
                <p><strong>Common Symptoms:</strong></p>
                <ul>
                    <li>Aching, heavy and uncomfortable legs</li>
                    <li>Swollen feet and ankles</li>
                    <li>Burning or throbbing sensation</li>
                    <li>Muscle cramp in your legs</li>
                    <li>Dry, itchy and thin skin over the affected vein</li>
                </ul>
                <p><strong>Treatment Options:</strong> Compression stockings, laser treatments, sclerotherapy, or surgery in severe cases.</p>
            </div>
        </div>
    </div>
''', unsafe_allow_html=True)