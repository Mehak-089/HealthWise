import pandas as pd
import numpy as np
import pickle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load datasets
df = pd.read_csv("dataset.csv")
severity_df = pd.read_csv("Symptom-severity.csv")
desc_df = pd.read_csv("symptom_Description.csv")
precaution_df = pd.read_csv("symptom_precaution.csv")

# Fill NaN values with "None"
df.fillna("None", inplace=True)

# Extract symptom columns
symptom_columns = [col for col in df.columns if "Symptom" in col]
all_symptoms = set()
for col in symptom_columns:
    all_symptoms.update(df[col].unique())

# Remove 'None' from symptom list
all_symptoms.discard("None")
all_symptoms = sorted(all_symptoms)

# Create a binary encoded DataFrame
encoded_data = pd.DataFrame(0, index=df.index, columns=all_symptoms)

# Populate the encoded DataFrame
for col in symptom_columns:
    for i, symptom in enumerate(df[col]):
        if symptom != "None":
            encoded_data.loc[i, symptom] = 1

# Add the disease column
encoded_data["Disease"] = df["Disease"]

# Split data into train and test sets
X = encoded_data.drop(columns=["Disease"])
y = encoded_data["Disease"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the Random Forest model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model
with open("disease_prediction_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model training complete and saved as 'disease_prediction_model.pkl'")
