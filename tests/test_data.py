import pytest
import pandas as pd
from unittest import mock
import sys
sys.path.append('../')
from src.data.load_data import load_data  # noqa: E402


@pytest.fixture
def mock_read_csv():
    with mock.patch('pandas.read_csv') as mock_csv:
        yield mock_csv


@pytest.fixture
def mock_glob():
    with mock.patch('glob.glob') as mock_glob:
        yield mock_glob


def test_load_data_with_matching_files(mock_read_csv, mock_glob):
    # Setup the mock for glob to simulate finding CSV files
    mock_glob.return_value = ['file1.csv', 'file2.csv']

    # Setup the mock for pandas read_csv to return a mock DataFrame
    mock_read_csv.side_effect = [
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}),  # Template DataFrame
        pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]}),  # file1.csv DataFrame
        pd.DataFrame({'col1': [9, 10], 'col2': [11, 12]})  # file2.csv DataFrame
    ]

    # Call load_data and get the final DataFrame
    result = load_data()

    # Assert that the final DataFrame has the expected data
    assert result.shape == (4, 2)  # Expecting 4 rows and 2 columns
    assert 'col1' in result.columns  # Assert that column 'col1' is present
    assert 'col2' in result.columns  # Assert that column 'col2' is present
    assert result['col1'].tolist() == [5, 6, 9, 10]  # Data from file1.csv and file2.csv
    assert result['col2'].tolist() == [7, 8, 11, 12]  # Data from file1.csv and file2.csv


def test_load_data_with_no_matching_files(mock_read_csv, mock_glob):
    # Setup the mock for glob to simulate no CSV files
    mock_glob.return_value = ['file1.csv', 'file2.csv']

    # Setup the mock for pandas read_csv to return a mock DataFrame
    mock_read_csv.side_effect = [
        pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}),  # Template DataFrame
        pd.DataFrame({'col3': [1, 2], 'col4': [3, 4]}),  # file1.csv DataFrame (no match)
        pd.DataFrame({'col5': [11, 12], 'col6': [13, 14]})  # file2.csv DataFrame (no match)
    ]

    # Call load_data and get the final DataFrame
    result = load_data()

    # Assert that the result is empty because no files matched the template
    print(result.head())
    assert result.empty  # The result should be an empty DataFrame


# Run the tests
if __name__ == '__main__':
    pytest.main()
