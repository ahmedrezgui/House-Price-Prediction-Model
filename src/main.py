# Import everything from the src package (i.e., from all the __init__.py files)
import os
import pickle
import sys

sys.path.append('../')

from src.models.train_model import train_model  # noqa: E402
from src.data.load_data import load_data  # noqa: E402


def main():
    # Step 1: Load data
    print("Loading data...")
    data = load_data()

    # Step 2: Train model
    print("Training model...")
    model = train_model(data)

    # Step 3: Save model
    print("Saving model...")
    MODEL_PATH = f"{os.getcwd()}\\models\\model.pkl"
    with open(MODEL_PATH, 'wb') as f:
        pickle.dump(model, f)

    print("Project completed successfully!")


if __name__ == "__main__":
    main()
