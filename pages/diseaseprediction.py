import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load the trained model
with open("disease_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load datasets
df = pd.read_csv("dataset.csv")
desc_df = pd.read_csv("symptom_Description.csv")

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

# Streamlit UI
st.title("Disease Prediction System")
st.write("Select your symptoms below:")

# Multi-select for symptoms
selected_symptoms = st.multiselect("Choose symptoms:", all_symptoms)

# Predict button
if st.button("Predict Disease"):
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
        st.success(f"Predicted Disease: {predicted_disease}")

        # Show disease description
        description = desc_df[desc_df["Disease"] == predicted_disease][
            "Description"
        ].values
        if description:
            st.info(f"Description: {description[0]}")
