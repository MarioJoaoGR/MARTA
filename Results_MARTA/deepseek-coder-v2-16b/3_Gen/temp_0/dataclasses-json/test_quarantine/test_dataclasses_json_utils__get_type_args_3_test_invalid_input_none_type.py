
import pytest
from dataclasses_json.utils import _get_type_args, _NO_ARGS
from typing import Tuple, Type, Union

def test_invalid_input_none_type():
    with pytest.raises(TypeError):
        _get_type_args(None)

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_3_test_invalid_input_none_type.py F [100%]

=================================== FAILURES ===================================
_________________________ test_invalid_input_none_type _________________________

    def test_invalid_input_none_type():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_3_test_invalid_input_none_type.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__get_type_args_3_test_invalid_input_none_type.py::test_invalid_input_none_type
============================== 1 failed in 0.05s ===============================
"""