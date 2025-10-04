import streamlit as st
import requests
import json
import os

# Backend API URL
API_URL = "http://127.0.0.1:8000/predict"

# Load city mappings from JSON file
CITY_MAPPING_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "utils", "city_mapping.json"
)


def load_city_mapping():
    """Loads city mapping from a JSON file."""
    try:
        with open(CITY_MAPPING_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        st.error("⚠️ Error: city_mapping.json not found.")
        return {}
    except json.JSONDecodeError:
        st.error("⚠️ Error: Invalid JSON format in city_mapping.json.")
        return {}
    except Exception as e:
        st.error(f"⚠️ Unexpected error loading city mapping: {e}")
        return {}


CITY_MAPPING = load_city_mapping()

# Ensure city mapping is valid
if not CITY_MAPPING:
    st.error("❌ No cities found. Please check city_mapping.json.")

# Streamlit UI
st.title("🏡 House Price Prediction")

# Collect input features
surface = st.number_input("Surface (m²)", min_value=10, max_value=5000, value=100)

selected_city = st.selectbox("Select a City", options=list(CITY_MAPPING.keys()))

rooms = st.number_input("Rooms", min_value=1, max_value=20, value=2)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=1)

# Checkbox options
parking = st.checkbox("Parking")
pool = st.checkbox("Pool")
vue_panoramique = st.checkbox("Panoramic View")
jardin = st.checkbox("Garden")
climatisation = st.checkbox("Air Conditioning")
chauffage_central = st.checkbox("Central Heating")
ascenseur = st.checkbox("Elevator")

# Convert booleans to 1/0
features = {
    "surface": surface,
    "city": selected_city,  # Send city name, backend converts it
    "rooms": rooms,
    "bathrooms": bathrooms,
    "parking": int(parking),
    "pool": int(pool),
    "vue_panoramique": int(vue_panoramique),
    "jardin": int(jardin),
    "climatisation": int(climatisation),
    "chauffage_central": int(chauffage_central),
    "ascenseur": int(ascenseur),
}

if st.button("Predict Price"):
    try:
        response = requests.post(API_URL, json=features)

        if response.status_code == 200:
            price = response.json().get("predicted_price", "N/A")
            st.success(f"💰 Predicted Price: {price} TND")
        else:
            st.error(f"❌ Error: {response.status_code} - {response.text}")

    except requests.exceptions.ConnectionError:
        st.error("🚨 Error: Could not connect to the API. Make sure the backend is running.")
