
import pytest
from io import StringIO
from pathlib import Path
from typing import Any, TextIO
from isort.api import Config, DEFAULT_CONFIG, check_stream

def test_valid_input():
    # Mock data for input stream
    code = """import os
import sys
"""
    input_stream = StringIO(code)
    
    # Call the function with valid input
    result = check_stream(input_stream, show_diff=False)
    
    # Assert that the result is True since we are not checking for differences in this test
    assert result is True
