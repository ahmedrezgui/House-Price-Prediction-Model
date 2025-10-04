import json
import os
from pydantic import BaseModel
from typing import Literal

# Load city mapping dynamically
CITY_MAPPING_PATH = os.path.join(
    os.path.dirname(__file__), "..", "..", "utils", "city_mapping.json"
)


def load_city_mapping():
    """Loads the city mapping from a JSON file."""
    try:
        with open(CITY_MAPPING_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("⚠️ Error: city_mapping.json not found.")
        return {}
    except json.JSONDecodeError:
        print("⚠️ Error: Invalid JSON format in city_mapping.json.")
        return {}
    except Exception as e:
        print(f"⚠️ Unexpected error loading city mapping: {e}")
        return {}


CITY_MAPPING = load_city_mapping()

# Ensure at least one city exists for Literal validation
CITY_KEYS = list(CITY_MAPPING.keys()) if CITY_MAPPING else ["unknown_city"]


class PredictionRequest(BaseModel):
    """Defines the expected input format for price prediction requests."""

    surface: float
    city: Literal[*CITY_KEYS]  # Restrict city names to predefined list
    rooms: int
    bathrooms: int
    parking: int
    pool: int
    vue_panoramique: int
    jardin: int
    climatisation: int
    chauffage_central: int
    ascenseur: int


class PredictionResponse(BaseModel):
    """Defines the response format for predicted prices."""

    predicted_price: float
