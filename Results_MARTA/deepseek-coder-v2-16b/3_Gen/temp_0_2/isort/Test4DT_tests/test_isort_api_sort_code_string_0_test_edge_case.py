
import pytest
from io import StringIO
from pathlib import Path
from isort.api import sort_code_string, Config, DEFAULT_CONFIG
from typing import Any, TextIO

# Assuming 'your_module_name' should be imported from isort.api
from unittest.mock import patch

def test_sort_code_string():
    code = """import os
import sys
import math
"""
    
    with patch('isort.api.StringIO', StringIO):
        sorted_code = sort_code_string(code)
        
    assert "math" in sorted_code
    assert "os" in sorted_code
    assert "sys" in sorted_code
