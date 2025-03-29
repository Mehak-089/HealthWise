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
injection_image_path = "pictures/injection.jpg"
influenza_image_path = "pictures/influenza.jpg"

encoded_logo = get_base64_image(logo_path)
encoded_injection = get_base64_image(injection_image_path)
encoded_influenza = get_base64_image(influenza_image_path)

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

<h2 class="upper-heading"><i>Disease Precautions</i></h2>

<div class="image-container">
    <img src="data:image/jpeg;base64,{encoded_injection}" alt="Injection Image">
</div>
""", unsafe_allow_html=True)

# --- Explore Our Features Section ---
st.markdown("""
<style>
    .subheading-section {
        padding: 60px;
        text-align: center;
        background-color: white;
        font-family: 'Poppins', sans-serif;
    }
    .subheading-heading {
        font-size: 40px;
        font-weight: bold;
        font-style: italic;
        color: #000000;
        margin-bottom: 20px;
    }
</style>
<div class="subheading-section">
    <div class="subheading-heading">Common Diseases and Precautions</div>
</div>
""", unsafe_allow_html=True)

# --- CSS Styles ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    body {
        font-family: 'Poppins', sans-serif;
    }

    .navbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background-color: white;
        padding: 15px 30px;
        border-bottom: 2px solid #ddd;
    }

    .navbar .app-name {
        font-size: 24px;
        font-weight: 600;
        color: #333;
        cursor: pointer;
    }

    .subheading-section {
        text-align: center;
        font-family: 'Poppins', sans-serif;
    }

    .subheading-heading {
        font-size: 30px;
        font-weight: bold;
        font-style: italic;
        margin-bottom: 20px;
    }

    .card-container {
        display: flex;
        align-items: center;
        gap: 20px;
        cursor: pointer;
        padding: 10px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        background-color: white;
        transition: all 0.3s ease-in-out;
        max-width: 500px;
    }

    .card-container:hover {
        box-shadow: 4px 4px 15px rgba(0, 0, 0, 0.3);
    }

    .card-container img {
        width: 80px;
        height: 80px;
        border-radius: 10px;
    }

    .disease-title {
        font-size: 20px;
        font-weight: bold;
        color: #333;
    }

    .expanded-card {
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
        background-color: white;
        width: 100%;
        max-width: 600px;
    }

    .expanded-card ul {
        text-align: left;
        padding-left: 20px;
    }

    .expanded-card li {
        font-size: 16px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

# --- Expandable Disease Card ---

# Initialize session state
if "expanded" not in st.session_state:
    st.session_state.expanded = False

# Function to toggle card state
def toggle_card():
    st.session_state.expanded = not st.session_state.expanded

# --- Display Card ---
st.markdown('<div class="subheading-heading">Common Diseases and Precautions</div>', unsafe_allow_html=True)


# Clickable card
if st.button("🤧 Achoo! Tell Me More", key="click_card"):
    toggle_card()

if not st.session_state.expanded:
    # Collapsed View: Show Image & Disease Name
    st.markdown(
        f"""
        <div class="card-container">
            <img src="data:image/jpeg;base64,{encoded_influenza}" alt="Influenza">
            <span class="disease-title">Influenza</span>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Expanded View: Show Details
    st.markdown(
        f"""
        <div class="expanded-card">
            <img src="data:image/jpeg;base64,{encoded_influenza}" alt="Influenza" style="width: 100%; border-radius: 10px;">
            <h2>Influenza</h2>
            <ul>
                <li>💉 <strong>Get Vaccinated</strong> – Annual flu shots help prevent infection.</li>
                <li>🧼 <strong>Practice Good Hygiene</strong> – Wash hands frequently with soap for at least 20 seconds.</li>
                <li>🤧 <strong>Cover Coughs & Sneezes</strong> – Use a tissue or your elbow to prevent spreading germs.</li>
                <li>🚫 <strong>Avoid Touching Face</strong> – Especially eyes, nose, and mouth to reduce infection risk.</li>
                <li>🏠 <strong>Stay Home if Sick</strong> – Prevent spreading the virus to others.</li>
                <li>🏥 <strong>Seek Medical Attention if Needed</strong> – Especially if symptoms worsen.</li>
                <li>💨 <strong>Ensure Good Ventilation</strong> – Open windows or use air purifiers to reduce airborne particles.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )