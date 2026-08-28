
import pytest
from unittest.mock import patch, MagicMock
from mimesis.providers.base import BaseProvider
import json
from pathlib import Path

# Assuming data_dir and datafile are defined somewhere in your script or configuration
data_dir = "path/to/your/data"  # Replace with the actual path to your data directory
datafile = "datafile.json"      # The name of the JSON file containing the data

def get_data(locale_name: str) -> dict:
    """Pull JSON data from file.

    :param locale_name: Locale name.
    :return: Content of JSON file as dict.
    """
    file_path = Path(data_dir).joinpath(locale_name, datafile)
    with open(file_path, 'r', encoding='utf8') as f:
        return json.load(f)

@patch('builtins.open', new_callable=MagicMock)
def test_get_data_with_valid_locale(mock_open):
    mock_file = MagicMock()
    mock_file.__enter__.return_value = mock_file
    mock_file.read.return_value = json.dumps({"key": "value"})
    mock_open.return_value = mock_file

    data = get_data("en_US")
    assert data == {"key": "value"}

@patch('builtins.open', new_callable=MagicMock)
def test_get_data_with_invalid_locale(mock_open):
    mock_file = MagicMock()
    mock_file.__enter__.return_value = mock_file
    mock_file.read.side_effect = FileNotFoundError("File not found")
    mock_open.return_value = mock_file

    with pytest.raises(FileNotFoundError):
        get_data("invalid_locale")
