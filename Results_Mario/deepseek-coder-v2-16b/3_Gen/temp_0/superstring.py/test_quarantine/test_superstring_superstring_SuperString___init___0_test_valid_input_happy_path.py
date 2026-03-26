
from superstring.superstring import SuperString

def test_valid_input_happy_path():
    s = SuperString("Hello, world!")
    
    # Test substring from start index to end of string
    assert s.substring(0) == "Hello, world!"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___0_test_valid_input_happy_path.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_happy_path __________________________

    def test_valid_input_happy_path():
        s = SuperString("Hello, world!")
    
        # Test substring from start index to end of string
>       assert s.substring(0) == "Hello, world!"
E       AssertionError: assert <superstring.superstring.SuperString object at 0x7f0c6a6b2650> == 'Hello, world!'
E        +  where <superstring.superstring.SuperString object at 0x7f0c6a6b2650> = substring(0)
E        +    where substring = <superstring.superstring.SuperString object at 0x7f0c6a6b2650>.substring

superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___0_test_valid_input_happy_path.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperString___init___0_test_valid_input_happy_path.py::test_valid_input_happy_path
============================== 1 failed in 0.04s ===============================
"""