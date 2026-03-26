
import io
import pytest
from flutes.io import _ReverseReadlineFile

# Test closing the file pointer in __exit__ method
def test_reverse_readlinefile_exit():
    def custom_generator():
        yield b'H'
        yield b'e'
        yield b'l'
        yield b'l'
        yield b'o'
    
    fp = io.BytesIO(b'Hello, World!')
    reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
    # Ensure the file pointer is not closed initially
    assert not fp.closed
    
    # Call __exit__ method to close the file pointer
    with pytest.raises(StopIteration):  # Since we are closing and generator will exhaust
        reverse_readline.__exit__(None, None, None)
    
    # Ensure the file pointer is closed after __exit__ is called
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1.py F [100%]

=================================== FAILURES ===================================
________________________ test_reverse_readlinefile_exit ________________________

    def test_reverse_readlinefile_exit():
        def custom_generator():
            yield b'H'
            yield b'e'
            yield b'l'
            yield b'l'
            yield b'o'
    
        fp = io.BytesIO(b'Hello, World!')
        reverse_readline = _ReverseReadlineFile(fp, custom_generator())
    
        # Ensure the file pointer is not closed initially
        assert not fp.closed
    
        # Call __exit__ method to close the file pointer
>       with pytest.raises(StopIteration):  # Since we are closing and generator will exhaust
E       Failed: DID NOT RAISE <class 'StopIteration'>

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1.py:22: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___exit___1.py::test_reverse_readlinefile_exit
============================== 1 failed in 0.09s ===============================
"""