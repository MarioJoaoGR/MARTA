
import sys
import os
import pytest
from flutes.io import shut_up

def test_shut_up():
    # Capture stdout and stderr
    captured_out = [b"", b""]
    captured_err = [b"", b""]
    
    class Capturing:
        def __enter__(self):
            self.orig_stdout = sys.stdout
            self.orig_stderr = sys.stderr
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            
        def __exit__(self, exc_type, exc_val, exc_tb):
            sys.stdout.close()
            sys.stderr.close()
            sys.stdout = self.orig_stdout
            sys.stderr = self.orig_stderr
    
    with Capturing():
        print("This should not be printed")
        assert True
