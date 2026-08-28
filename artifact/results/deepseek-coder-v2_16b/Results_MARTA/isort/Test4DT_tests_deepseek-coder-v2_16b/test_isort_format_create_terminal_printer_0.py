
import pytest
from io import StringIO
from isort.format import create_terminal_printer
import sys

def test_invalid_input_missing_colorama():
    # Create a mock output object that simulates standard error (stderr)
    fake_output = StringIO()
    
    # Capture the original stderr to restore it after the test
    original_stderr = sys.stderr
    sys.stderr = fake_output
    
    try:
        create_terminal_printer(True, None)
    except SystemExit as e:
        assert str(e) == "1"
    finally:
        # Restore the original stderr
        sys.stderr = original_stderr
