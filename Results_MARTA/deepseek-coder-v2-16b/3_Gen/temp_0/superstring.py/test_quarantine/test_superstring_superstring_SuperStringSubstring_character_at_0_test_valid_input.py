
from superstring.superstring import SuperStringSubstring, SuperStringBase

def test_valid_input():
    base = "Hello, World!"
    start_index = 7
    end_index = 12
    setup = SuperStringSubstring(base, start_index, end_index)
    assert setup.character_at(0) == 'W'

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_character_at_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        base = "Hello, World!"
        start_index = 7
        end_index = 12
        setup = SuperStringSubstring(base, start_index, end_index)
>       assert setup.character_at(0) == 'W'

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_character_at_0_test_valid_input.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringSubstring object at 0x7f9b136b5950>
index = 0

    def character_at(self, index):
>       return self._base.character_at(self._start_index + index)
E       AttributeError: 'str' object has no attribute 'character_at'

superstring.py/superstring/superstring.py:130: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringSubstring_character_at_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""