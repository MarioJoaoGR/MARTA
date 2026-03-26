
import pytest
from pathlib import Path
import io
from flutes.io import reverse_open

# Test cases for reverse_open function
def test_reverse_open_default():
    with pytest.raises(ValueError):
        list(reverse_open('nonexistentfile.txt'))  # Should raise ValueError due to non-existent file

def test_reverse_open_with_encoding():
    with pytest.raises(ValueError):
        list(reverse_open('nonexistentfile.txt', encoding='ascii'))  # Should raise ValueError due to non-existent file

def test_reverse_open_with_allow_empty_lines():
    with open('testfile.txt', 'w') as f:
        f.write("Line1\nLine2\n")
    result = list(reverse_open('testfile.txt', allow_empty_lines=True))
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

flutes/Test4DT_tests/test_flutes_io_reverse_open_0.py FF.                [100%]

=================================== FAILURES ===================================
__________________________ test_reverse_open_default ___________________________

    def test_reverse_open_default():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_io_reverse_open_0.py:9: Failed
_______________________ test_reverse_open_with_encoding ________________________

    def test_reverse_open_with_encoding():
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

flutes/Test4DT_tests/test_flutes_io_reverse_open_0.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_0.py::test_reverse_open_default
FAILED flutes/Test4DT_tests/test_flutes_io_reverse_open_0.py::test_reverse_open_with_encoding
========================= 2 failed, 1 passed in 0.10s ==========================
"""