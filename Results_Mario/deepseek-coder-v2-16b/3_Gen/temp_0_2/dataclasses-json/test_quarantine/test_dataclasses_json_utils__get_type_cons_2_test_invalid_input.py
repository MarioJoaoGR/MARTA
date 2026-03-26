
import pytest
from dataclasses_json.utils import _get_type_cons

def test_invalid_input():
    with pytest.raises(TypeError):
        result = _get_type_cons('not a valid type')

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
>           result = _get_type_cons('not a valid type')

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_2_test_invalid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

type_ = 'not a valid type'

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
E           AttributeError: 'str' object has no attribute '__origin__'

dataclasses-json/dataclasses_json/utils.py:28: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_cons_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.04s ===============================
"""