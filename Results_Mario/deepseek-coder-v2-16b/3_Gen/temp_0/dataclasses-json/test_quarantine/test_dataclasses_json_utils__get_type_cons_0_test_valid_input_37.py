
from dataclasses_json.utils import _get_type_cons
import pytest
import sys

@pytest.mark.skipif(sys.version_info < (3, 7), reason="Requires Python 3.7 or higher")
def test_valid_input_3_7():
    my_list = [1, 2, 3]
    type_obj = my_list.__class__
    expected_cons = list  # Note: The constructor for `list` is indeed 'list' in Python.
    
    result = _get_type_cons(type_obj)
    
    assert result == expected_cons, f"Expected {expected_cons}, but got {result}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/dataclasses-json
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0_test_valid_input_37.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_input_3_7 _____________________________

    @pytest.mark.skipif(sys.version_info < (3, 7), reason="Requires Python 3.7 or higher")
    def test_valid_input_3_7():
        my_list = [1, 2, 3]
        type_obj = my_list.__class__
        expected_cons = list  # Note: The constructor for `list` is indeed 'list' in Python.
    
>       result = _get_type_cons(type_obj)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0_test_valid_input_37.py:12: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = <class 'list'>

    def _get_type_cons(type_):
        """More spaghetti logic for 3.6 vs. 3.7"""
        if sys.version_info.minor == 6:
            try:
                cons = type_.__extra__
            except AttributeError:
                try:
                    cons = type_.__origin__
                except AttributeError:
                    cons = type_
                else:
                    cons = type_ if cons is None else cons
            else:
                try:
                    cons = type_.__origin__ if cons is None else cons
                except AttributeError:
                    cons = type_
        else:
>           cons = type_.__origin__
E           AttributeError: type object 'list' has no attribute '__origin__'

dataclasses-json/dataclasses_json/utils.py:28: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0_test_valid_input_37.py::test_valid_input_3_7
============================== 1 failed in 0.05s ===============================
"""