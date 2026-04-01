
import pytest
import sys
from dataclasses_json.utils import _get_type_cons

@pytest.mark.skipif(sys.version_info < (3, 6), reason="This test only runs on Python 3.6")
def test_valid_input_3_6():
    my_list = [1, 2, 3]
    type_obj = my_list.__class__
    cons = _get_type_cons(type_obj)
    assert cons == list

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0_test_valid_input_36.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_valid_input_3_6 _____________________________

    @pytest.mark.skipif(sys.version_info < (3, 6), reason="This test only runs on Python 3.6")
    def test_valid_input_3_6():
        my_list = [1, 2, 3]
        type_obj = my_list.__class__
>       cons = _get_type_cons(type_obj)

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0_test_valid_input_36.py:10: 
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
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_0_test_valid_input_36.py::test_valid_input_3_6
============================== 1 failed in 0.04s ===============================
"""