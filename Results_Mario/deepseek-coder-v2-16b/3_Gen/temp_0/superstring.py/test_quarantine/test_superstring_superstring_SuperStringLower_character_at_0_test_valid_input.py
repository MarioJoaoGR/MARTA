
import pytest
from superstring.superstring import SuperStringBase  # Assuming this is the correct module path
from superstring.superstring import SuperStringLower

def test_valid_input():
    base = SuperStringBase('Hello, World!')
    super_string = SuperStringLower(base)
    
    assert super_string.character_at(0) == 'h'
    assert super_string.character_at(1) == 'e'
    assert super_string.character_at(7) == 'w'
    assert super_string.character_at(12) == '!'

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
>       base = SuperStringBase('Hello, World!')
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0_test_valid_input.py:7: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.04s ===============================
"""