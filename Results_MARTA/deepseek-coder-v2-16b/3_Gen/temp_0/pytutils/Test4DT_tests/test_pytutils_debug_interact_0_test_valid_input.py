
import pytest
import sys
from io import StringIO
from unittest.mock import patch
from pytutils.debug import interact

def test_valid_input():
    def test():
        x = 10
        y = 20
        interact()
    
    # Capture the output of the function to ensure it runs without errors
    captured_output = []
    def capture_output(func):
        def wrapper(*args, **kwargs):
            import sys
            from io import StringIO
            old_stdout = sys.stdout
            new_stdout = StringIO()
            sys.stdout = new_stdout
            func(*args, **kwargs)
            captured_output.append(new_stdout.getvalue())
            sys.stdout = old_stdout
        return wrapper
    
    @capture_output
    def run_test():
        test()
    
    with patch('sys.stdin', StringIO()):  # Mock stdin to avoid reading from it
        run_test()
    
    assert captured_output, "Expected output was not captured"
