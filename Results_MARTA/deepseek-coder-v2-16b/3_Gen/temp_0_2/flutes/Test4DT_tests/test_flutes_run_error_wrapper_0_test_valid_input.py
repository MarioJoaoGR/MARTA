
import subprocess
from unittest.mock import patch
import pytest
from flutes.run import error_wrapper

def test_valid_input():
    class MockCalledProcessError(Exception):
        def __init__(self, returncode, cmd, output=None):
            self.returncode = returncode
            self.cmd = cmd
            self.output = output
        
        def __str__(self):
            string = super().__str__()
            if self.output:
                try:
                    output = self.output.decode('utf-8')
                except UnicodeEncodeError:  # ignore output
                    string += "\nFailed to parse output."
                else:
                    string += "\nCaptured output:\n" + '\n'.join([f'    {line}' for line in output.split('\n')])
            else:
                string += "\nNo output was generated."
            return string

    with patch('subprocess.run', side_effect=MockCalledProcessError(1, ['false'], b"output")):
        try:
            subprocess.run(['false'], capture_output=True, text=True)
        except Exception as e:
            wrapped_error = error_wrapper(e)
            assert "Captured output:\n    output" in str(wrapped_error)
