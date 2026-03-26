
import pytest
from pytutils.files import burp
import sys
import os

@pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars", [
    ("-", "Hello, world!", 'w', True, False, False),  # Test writing to stdout
    ("example.txt", "Hello, world!", 'w', False, True, True),  # Test expanding user home directory and environment variables in filename
    (None, "Test contents", 'w', True, True, True)  # Invalid input for filename should raise an error
])
def test_invalid_input(filename, contents, mode, allow_stdout, expanduser, expandvars):
    with pytest.raises(TypeError):
        burp(filename, contents, mode=mode, allow_stdout=allow_stdout, expanduser=expanduser, expandvars=expandvars)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_invalid_input.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
____________ test_invalid_input[--Hello, world!-w-True-False-False] ____________

filename = '-', contents = 'Hello, world!', mode = 'w', allow_stdout = True
expanduser = False, expandvars = False

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars", [
        ("-", "Hello, world!", 'w', True, False, False),  # Test writing to stdout
        ("example.txt", "Hello, world!", 'w', False, True, True),  # Test expanding user home directory and environment variables in filename
        (None, "Test contents", 'w', True, True, True)  # Invalid input for filename should raise an error
    ])
    def test_invalid_input(filename, contents, mode, allow_stdout, expanduser, expandvars):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_invalid_input.py:13: Failed
----------------------------- Captured stdout call -----------------------------
Hello, world!
_______ test_invalid_input[example.txt-Hello, world!-w-False-True-True] ________

filename = 'example.txt', contents = 'Hello, world!', mode = 'w'
allow_stdout = False, expanduser = True, expandvars = True

    @pytest.mark.parametrize("filename, contents, mode, allow_stdout, expanduser, expandvars", [
        ("-", "Hello, world!", 'w', True, False, False),  # Test writing to stdout
        ("example.txt", "Hello, world!", 'w', False, True, True),  # Test expanding user home directory and environment variables in filename
        (None, "Test contents", 'w', True, True, True)  # Invalid input for filename should raise an error
    ])
    def test_invalid_input(filename, contents, mode, allow_stdout, expanduser, expandvars):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_invalid_input.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_invalid_input.py::test_invalid_input[--Hello, world!-w-True-False-False]
FAILED pytutils/Test4DT_tests/test_pytutils_files_burp_2_test_invalid_input.py::test_invalid_input[example.txt-Hello, world!-w-False-True-True]
========================= 2 failed, 1 passed in 0.07s ==========================
"""