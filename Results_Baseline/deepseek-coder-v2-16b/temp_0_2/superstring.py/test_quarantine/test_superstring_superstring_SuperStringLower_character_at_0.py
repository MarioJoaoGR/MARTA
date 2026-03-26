
import pytest
from superstring.superstring import SuperStringLower

# Test case for initializing the class with a string
def test_init():
    obj = SuperStringLower("Hello World")
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/superstring.py
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 3 items

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
__________________________________ test_init ___________________________________

    def test_init():
        obj = SuperStringLower("Hello World")
>       assert obj._base == "hello world"
E       AssertionError: assert 'Hello World' == 'hello world'
E         
E         - hello world
E         ? ^     ^
E         + Hello World
E         ? ^     ^

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0.py:8: AssertionError
_____________________________ test_init_non_string _____________________________

    def test_init_non_string():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0.py:12: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0.py::test_init
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_character_at_0.py::test_init_non_string
========================= 2 failed, 1 passed in 0.06s ==========================
"""