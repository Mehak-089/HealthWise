import streamlit as st
import pickle
import pandas as pd
import numpy as np
import base64

# Set page configuration
st.set_page_config(page_title="HealthWise", layout="wide")

# Load and encode images
logo_path = "pictures/logo.jpg"
hero_image_path = "pictures/fp.jpg"

def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Encode images (handle cases where images might not exist)
try:
    encoded_logo = get_base64_image(logo_path)
    encoded_hero_image = get_base64_image(hero_image_path)
except FileNotFoundError:
    encoded_logo = ""
    encoded_hero_image = ""

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

# Display the UI components
st.markdown(navbar_html, unsafe_allow_html=True)
st.markdown(hero_section_html, unsafe_allow_html=True)

# --- Disease Prediction System Section ---
disease_prediction_section_html = """
<style>
    .disease-prediction-section {
        padding: 60px;
        text-align: center;
        background-color: #f9f9f9;
        font-family: 'Poppins', sans-serif;
    }
    .disease-prediction-heading {
        font-size: 40px;
        font-weight: bold;
        color: black;
        margin-bottom: 20px;
        text-align: center;
    }
</style>
<div class="disease-prediction-section">
    <div class="disease-prediction-heading">Disease Prediction System</div>
</div>
"""

# Display the disease prediction section header
st.markdown(disease_prediction_section_html, unsafe_allow_html=True)

# Load the trained model
try:
    with open("disease_prediction_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'disease_prediction_model.pkl' exists.")
    st.stop()

# Load datasets
try:
    df = pd.read_csv("dataset.csv")
    desc_df = pd.read_csv("symptom_Description.csv")
except FileNotFoundError:
    st.error("Dataset files not found. Please ensure 'dataset.csv' and 'symptom_Description.csv' exist.")
    st.stop()

# Extract symptom columns
symptom_columns = [col for col in df.columns if "Symptom" in col]
all_symptoms = set()

for col in symptom_columns:
    all_symptoms.update(
        str(symptom) for symptom in df[col].unique()
    )  # Convert to string

# Remove 'None' and 'nan' if present
all_symptoms.discard("None")
all_symptoms.discard("nan")  # Handles NaN values

# Convert to sorted list
all_symptoms = sorted(all_symptoms)

# Prediction UI
st.markdown('<h3 style="color: #404040;">Select your symptoms below:</h3>', unsafe_allow_html=True)
selected_symptoms = st.multiselect("Choose symptoms:", all_symptoms, label_visibility="collapsed")
    
if st.button("Predict Disease", use_container_width=True):
    if not selected_symptoms:
        st.warning("Please select at least one symptom.")
    else:
        # Create input data for prediction
        input_data = np.zeros(len(all_symptoms))
        for symptom in selected_symptoms:
            if symptom in all_symptoms:
                input_data[list(all_symptoms).index(symptom)] = 1

        # Reshape input and predict
        input_data = input_data.reshape(1, -1)
        predicted_disease = model.predict(input_data)[0]

        # Display results
        st.success(f"**Predicted Disease:** {predicted_disease}")

        # Show disease description
        description = desc_df[desc_df["Disease"] == predicted_disease][
            "Description"
        ].values
        if len(description) > 0:
            st.info(f"**Description:** {description[0]}")
        else:
            st.warning("No description available for this disease.")