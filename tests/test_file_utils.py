import pytest
import sys
sys.path.append('../')
from utils.file_utils.file_utils import getUnprocessedDataSetFilePath, getProcessedDataSetFilePath, getSaveUtilsFilePath  # noqa: E402 # Ignore import error


@pytest.mark.parametrize("file_name, repository_path, expected", [
    ("data.csv", "C:\\Users\\user\\project", "C:\\Users\\user\\project\\data\\raw\\data.csv")
])
def test_getUnprocessedDataSetFilePath(file_name, repository_path, expected):
    result = getUnprocessedDataSetFilePath(file_name, repository_path)
    assert result == expected


@pytest.mark.parametrize("file_name, repository_path, expected", [
    ("data.csv", "C:\\Users\\user\\project", "C:\\Users\\user\\project\\data\\processed\\data.csv")
])
def test_getProcessedDataSetFilePath(file_name, repository_path, expected):
    result = getProcessedDataSetFilePath(file_name, repository_path)
    assert result == expected


@pytest.mark.parametrize("file_name, repository_path, expected", [
    ("utils.py", "C:\\Users\\user\\project", "C:\\Users\\user\\project\\utils\\utils.py")
])
def test_getSaveUtilsFilePath(file_name, repository_path, expected):
    result = getSaveUtilsFilePath(repository_path, file_name)
    assert result == expected
