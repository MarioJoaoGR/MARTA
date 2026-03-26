
import pytest
from superstring.superstring import SuperStringBase

def test_valid_strip():
    obj = SuperStringBase()
    obj.content = "  Hello, World!  "
    stripped_str = obj.strip()
    assert stripped_str == "Hello, World!"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_strip_0_test_valid_strip.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_strip _______________________________

    def test_valid_strip():
        obj = SuperStringBase()
        obj.content = "  Hello, World!  "
>       stripped_str = obj.strip()

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_strip_0_test_valid_strip.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringBase object at 0x7f89c6804fd0>

    def strip(self):
>       for start_index in range(self.length()):
E       TypeError: 'NoneType' object cannot be interpreted as an integer

superstring.py/superstring/superstring.py:46: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringBase_strip_0_test_valid_strip.py::test_valid_strip
============================== 1 failed in 0.04s ===============================
"""