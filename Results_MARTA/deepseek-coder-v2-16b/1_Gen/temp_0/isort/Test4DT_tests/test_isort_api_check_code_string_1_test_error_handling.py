
from io import StringIO
from unittest.mock import patch
import pytest
from isort.api import check_code_string, Config, DEFAULT_CONFIG

def test_check_code_string():
    code = "import os\nimport sys"
    with patch('isort.api.Config') as mock_config:
        # Mock the behavior of Config to return a default instance
        mock_config.return_value = Config()
        
        result = check_code_string(code, show_diff=False)
        assert result is True, "The code string should be correctly checked"
