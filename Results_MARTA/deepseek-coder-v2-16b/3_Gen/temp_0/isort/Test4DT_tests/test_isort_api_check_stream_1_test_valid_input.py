
from io import StringIO

import pytest

from isort import Config
from isort.api import check_stream


def test_valid_input():
    # Mock data for input stream
    code = """import os
import sys"""
    
    # Create a mock file-like object for the input stream
    input_stream = StringIO(code)
    
    # Call the function with the mock input stream and check that it returns True
    result = check_stream(input_stream, show_diff=False)
    
    assert result is True
