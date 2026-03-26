
import pytest
from unittest.mock import MagicMock
from superstring.superstring import SuperStringConcatenation

@pytest.fixture
def setup_concatenation():
    left = MagicMock()
    right = MagicMock()
    return SuperStringConcatenation(left, right)

def test_to_printable_default(setup_concatenation):
    concatenation = setup_concatenation
    concatenation._left.to_printable.return_value = "Hello"
    concatenation._right.to_printable.return_value = "World!"
    
    result = concatenation.to_printable()
    assert result == "HelloWorld!"

def test_to_printable_with_start_index(setup_concatenation):
    concatenation = setup_concatenation
    concatenation._left.to_printable.return_value = "Hello"
    concatenation._right.to_printable.return_value = "World!"
    
    result = concatenation.to_printable(start_index=6)
    assert result == "World!"

def test_to_printable_with_end_index(setup_concatenation):
    concatenation = setup_concatenation
    concatenation._left.to_printable.return_value = "Hello"
    concatenation._right.to_printable.return_value = "World!"
    
    result = concatenation.to_printable(end_index=5)
    assert result == "Hello"

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

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_edge_case.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
__________________________ test_to_printable_default ___________________________

setup_concatenation = <superstring.superstring.SuperStringConcatenation object at 0x7fd2a06bd250>

    def test_to_printable_default(setup_concatenation):
        concatenation = setup_concatenation
        concatenation._left.to_printable.return_value = "Hello"
        concatenation._right.to_printable.return_value = "World!"
    
>       result = concatenation.to_printable()

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_edge_case.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringConcatenation object at 0x7fd2a06bd250>
start_index = 0
end_index = <MagicMock name='mock.length().__add__()' id='140542606493456'>

    def to_printable(self, start_index=None, end_index=None):
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        left_len = self._left.length()
>       if end_index < left_len:
E       TypeError: '<' not supported between instances of 'MagicMock' and 'MagicMock'

superstring.py/superstring/superstring.py:112: TypeError
______________________ test_to_printable_with_start_index ______________________

setup_concatenation = <superstring.superstring.SuperStringConcatenation object at 0x7fd2a019e610>

    def test_to_printable_with_start_index(setup_concatenation):
        concatenation = setup_concatenation
        concatenation._left.to_printable.return_value = "Hello"
        concatenation._right.to_printable.return_value = "World!"
    
>       result = concatenation.to_printable(start_index=6)

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_edge_case.py:25: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringConcatenation object at 0x7fd2a019e610>
start_index = 6
end_index = <MagicMock name='mock.length().__add__()' id='140542606650448'>

    def to_printable(self, start_index=None, end_index=None):
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        left_len = self._left.length()
>       if end_index < left_len:
E       TypeError: '<' not supported between instances of 'MagicMock' and 'MagicMock'

superstring.py/superstring/superstring.py:112: TypeError
_______________________ test_to_printable_with_end_index _______________________

setup_concatenation = <superstring.superstring.SuperStringConcatenation object at 0x7fd2a07d6790>

    def test_to_printable_with_end_index(setup_concatenation):
        concatenation = setup_concatenation
        concatenation._left.to_printable.return_value = "Hello"
        concatenation._right.to_printable.return_value = "World!"
    
>       result = concatenation.to_printable(end_index=5)

superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_edge_case.py:33: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <superstring.superstring.SuperStringConcatenation object at 0x7fd2a07d6790>
start_index = 0, end_index = 5

    def to_printable(self, start_index=None, end_index=None):
        start_index = start_index if start_index is not None else 0
        end_index = end_index if end_index is not None else self.length()
        left_len = self._left.length()
>       if end_index < left_len:
E       TypeError: '<' not supported between instances of 'int' and 'MagicMock'

superstring.py/superstring/superstring.py:112: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_edge_case.py::test_to_printable_default
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_edge_case.py::test_to_printable_with_start_index
FAILED superstring.py/Test4DT_tests/test_superstring_superstring_SuperStringConcatenation_to_printable_0_test_edge_case.py::test_to_printable_with_end_index
============================== 3 failed in 0.06s ===============================
"""