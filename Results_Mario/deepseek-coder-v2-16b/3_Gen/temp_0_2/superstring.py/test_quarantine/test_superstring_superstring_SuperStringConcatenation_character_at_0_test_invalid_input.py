
import pytest
from superstring.superstring import SuperStringConcatenation, SuperStringBase

def test_invalid_input():
    with pytest.raises(TypeError):
        ssc = SuperStringConcatenation("Hello", "World")
        ssc.character_at("invalid index")  # This should raise a TypeError

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
            ssc = SuperStringConcatenation("Hello", "World")
>           ssc.character_at("invalid index")  # This should raise a TypeError

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_invalid_input.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringConcatenation object at 0x7fd1e6fc5ad0>
index = 'invalid index'

    def character_at(self, index):
>       left_len = self._left.length()
E       AttributeError: 'str' object has no attribute 'length'

superstring.py/superstring/superstring.py:103: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_character_at_0_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.05s ===============================
"""