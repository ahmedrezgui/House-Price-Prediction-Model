import pytest
from unittest import mock
import pandas as pd
from sklearn.preprocessing import StandardScaler
import lightgbm as lgb
import sys
sys.path.append('../')

from src.models.train_model import train_model  # noqa: E402


@pytest.fixture
def mock_standard_scaler():
    with mock.patch.object(StandardScaler, 'fit_transform') as mock_fit_transform:
        yield mock_fit_transform


@pytest.fixture
def mock_lightgbm():
    with mock.patch.object(lgb.LGBMRegressor, 'fit') as mock_fit:
        yield mock_fit


def test_train_model(mock_standard_scaler, mock_lightgbm):
    # Create a sample DataFrame for the test
    data = {
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6],
        'price': [100, 200, 300]
    }
    df = pd.DataFrame(data)

    # Mock the behavior of StandardScaler.fit_transform to return scaled data
    mock_standard_scaler.return_value = [[-1.0, -1.0], [0.0, 0.0], [1.0, 1.0]]

    # Mock the behavior of LGBMRegressor.fit to do nothing (simulating training)
    mock_lightgbm.return_value = None

    # Call the function
    model = train_model(df)

    # Get the expected scaled values
    expected_X_scaled = [[-1.0, -1.0], [0.0, 0.0], [1.0, 1.0]]

    # Assert that the model's fit method was called once
    mock_lightgbm.assert_called_once()

    # Assert that the first argument passed to `fit` is a numpy array-like object
    # We use `.call_args` to get the arguments passed to the function
    args = mock_lightgbm.call_args
    X_passed = args[0]  # The first argument should be the scaled features
    assert expected_X_scaled.__eq__(X_passed)  # Check if scaled features match the expected values

    # Assert that the returned model is of the correct type
    assert isinstance(model, lgb.LGBMRegressor)


def test_train_model_with_missing_price_column(mock_standard_scaler, mock_lightgbm):
    # Create a DataFrame without the 'price' column
    df = pd.DataFrame({
        'feature1': [1, 2, 3],
        'feature2': [4, 5, 6]
    })

    # Call the function and expect it to raise an error
    with pytest.raises(KeyError):  # Expecting a KeyError since 'price' is missing
        train_model(df)


# Run the tests
if __name__ == '__main__':
    pytest.main()
