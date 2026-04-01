
import pytest
from flutes.io import _ReverseReadlineFile
import io

def test_invalid_input():
    # Test with non-file-like object
    fp = "not a file-like object"
    gen = lambda: iter([])
    
    with pytest.raises(TypeError):
        with _ReverseReadlineFile(fp, gen()) as rrlf:
            pass

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

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Test with non-file-like object
        fp = "not a file-like object"
        gen = lambda: iter([])
    
        with pytest.raises(TypeError):
>           with _ReverseReadlineFile(fp, gen()) as rrlf:

flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_invalid_input.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
flutes/flutes/io.py:229: in __exit__
    self.close()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <flutes.io._ReverseReadlineFile object at 0x7f63fe81fd50>

    def close(self):
>       self.fp.close()
E       AttributeError: 'str' object has no attribute 'close'

flutes/flutes/io.py:235: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile___enter___0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.10s ===============================
"""