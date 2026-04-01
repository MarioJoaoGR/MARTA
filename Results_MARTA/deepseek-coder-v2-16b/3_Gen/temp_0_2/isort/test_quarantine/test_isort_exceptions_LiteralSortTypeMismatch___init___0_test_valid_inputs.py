
import pytest
from isort.exceptions import LiteralSortTypeMismatch

def test_valid_inputs():
    # Test case 1: kind is int, expected_kind is str
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(int, str)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'int'>."
    
    # Test case 2: kind is float, expected_kind is int
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch(float, int)
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'float'>."
    
    # Test case 3: kind is list, expected_kind is tuple
    with pytest.raises(LiteralSortTypeMismatch) as excinfo:
        raise LiteralSortTypeMismatch([], ())
    assert str(excinfo.value) == "isort was told to sort a literal of type <class 'tuple'> but was given a literal of type <class 'list'>."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_exceptions_LiteralSortTypeMismatch___init___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test case 1: kind is int, expected_kind is str
        with pytest.raises(LiteralSortTypeMismatch) as excinfo:
            raise LiteralSortTypeMismatch(int, str)
        assert str(excinfo.value) == "isort was told to sort a literal of type <class 'str'> but was given a literal of type <class 'int'>."
    
        # Test case 2: kind is float, expected_kind is int
        with pytest.raises(LiteralSortTypeMismatch) as excinfo:
            raise LiteralSortTypeMismatch(float, int)
        assert str(excinfo.value) == "isort was told to sort a literal of type <class 'int'> but was given a literal of type <class 'float'>."
    
        # Test case 3: kind is list, expected_kind is tuple
        with pytest.raises(LiteralSortTypeMismatch) as excinfo:
            raise LiteralSortTypeMismatch([], ())
>       assert str(excinfo.value) == "isort was told to sort a literal of type <class 'tuple'> but was given a literal of type <class 'list'>."
E       assert 'isort was to...l of type [].' == "isort was to...lass 'list'>."
E         
E         - isort was told to sort a literal of type <class 'tuple'> but was given a literal of type <class 'list'>.
E         ?                                          ^^^^^^^^^^^^^^^                                 ^^^^^^^^^^^^^^
E         + isort was told to sort a literal of type () but was given a literal of type [].
E         ?                                          ^^                                 ^^

isort/Test4DT_tests/test_isort_exceptions_LiteralSortTypeMismatch___init___0_test_valid_inputs.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_LiteralSortTypeMismatch___init___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.09s ===============================
"""