# src/__init__.py
from .data import load_data
from .models import train_model


__all__ = [
    "load_data",
    "train_model"
]
