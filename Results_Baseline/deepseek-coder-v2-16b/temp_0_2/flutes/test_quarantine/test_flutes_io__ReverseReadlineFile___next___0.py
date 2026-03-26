
import io
import pytest
from flutes.io import _ReverseReadlineFile

# Test cases for __init__ method
def test_init_with_file_like_object():
    file_obj = io.StringIO("Line1\nLine2\nLine3\n")
    
    def reverse_gen(fp):
        while True:
            line = fp.readline()
            if not line:
                break
            yield line
    
    rev_reader = _ReverseReadlineFile(fp=file_obj, gen=reverse_gen(file_obj))
    
    assert next(rev_reader) == "Line3\n"
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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0.py F [100%]

=================================== FAILURES ===================================
_______________________ test_init_with_file_like_object ________________________

    def test_init_with_file_like_object():
        file_obj = io.StringIO("Line1\nLine2\nLine3\n")
    
        def reverse_gen(fp):
            while True:
                line = fp.readline()
                if not line:
                    break
                yield line
    
        rev_reader = _ReverseReadlineFile(fp=file_obj, gen=reverse_gen(file_obj))
    
>       assert next(rev_reader) == "Line3\n"
E       AssertionError: assert 'Line1\n\n' == 'Line3\n'
E         
E         - Line3
E         ?     ^
E         + Line1
E         ?     ^
E         +

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___next___0.py::test_init_with_file_like_object
============================== 1 failed in 0.10s ===============================
"""