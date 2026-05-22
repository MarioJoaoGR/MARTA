
import json
from pathlib import Path
from typing import Dict, Any
from httpie.config import read_raw_config, ConfigFileError
import unittest.mock as mock

def test_valid_input():
    # Define a sample configuration file content
    config_content = {
        "key": "value"
    }
    
    # Create a temporary file with the sample content
    temp_file_path = Path("temp_config.json")
    with open(temp_file_path, 'w') as f:
        json.dump(config_content, f)
    
    try:
        # Use mock to simulate opening and reading the file
        with mock.patch('builtins.open', mock.mock_open(read_data=json.dumps(config_content))):
            result = read_raw_config('settings', temp_file_path)
            assert result == config_content
    finally:
        # Clean up the temporary file
        if temp_file_path.exists():
            temp_file_path.unlink()
