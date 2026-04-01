
from superstring.superstring import SuperStringUpper, SuperStringBase

def test_invalid_input():
    # Create an instance of SuperStringUpper with a base string
    super_string = SuperStringUpper(SuperStringBase('Hello, World!'))
    
    # Test the character_at method with an invalid index (negative index)
    assert super_string.character_at(-1) == ''

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        # Create an instance of SuperStringUpper with a base string
>       super_string = SuperStringUpper(SuperStringBase('Hello, World!'))
E       TypeError: SuperStringBase() takes no arguments

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_2_test_invalid_input.py:6: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringUpper_character_at_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""