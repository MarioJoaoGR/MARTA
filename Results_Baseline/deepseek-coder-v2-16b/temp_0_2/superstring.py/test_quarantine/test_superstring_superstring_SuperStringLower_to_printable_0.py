
# Module: superstring.superstring
import pytest
from superstring.superstring import SuperStringLower

# Test initialization with a string
def test_initialization():
    obj = SuperStringLower("Hello World")
    assert obj._base == "hello world"

# Test providing a non-string value during initialization
def test_initialization_non_string():
    with pytest.raises(TypeError):
        SuperStringLower(12345)

# Test calling the `to_printable` method without indices
def test_to_printable_without_indices():
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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_____________________________ test_initialization ______________________________

    def test_initialization():
        obj = SuperStringLower("Hello World")
>       assert obj._base == "hello world"
E       AssertionError: assert 'Hello World' == 'hello world'
E         
E         - hello world
E         ? ^     ^
E         + Hello World
E         ? ^     ^

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py:9: AssertionError
________________________ test_initialization_non_string ________________________

    def test_initialization_non_string():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py::test_initialization
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringLower_to_printable_0.py::test_initialization_non_string
========================= 2 failed, 1 passed in 0.05s ==========================
"""