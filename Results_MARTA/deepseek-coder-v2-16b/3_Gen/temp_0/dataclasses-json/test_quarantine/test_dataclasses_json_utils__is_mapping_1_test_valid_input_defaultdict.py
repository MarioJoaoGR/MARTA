
from collections import defaultdict
import pytest
from dataclasses_json.utils import _is_mapping, _get_type_origin, _issubclass_safe
from typing import Mapping

def test_valid_input_defaultdict():
    my_defaultdict = defaultdict(int)
    assert _is_mapping(my_defaultdict), "Expected defaultdict to be identified as a mapping"

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

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_1_test_valid_input_defaultdict.py F [100%]

=================================== FAILURES ===================================
_________________________ test_valid_input_defaultdict _________________________

    def test_valid_input_defaultdict():
        my_defaultdict = defaultdict(int)
>       assert _is_mapping(my_defaultdict), "Expected defaultdict to be identified as a mapping"
E       AssertionError: Expected defaultdict to be identified as a mapping
E       assert False
E        +  where False = _is_mapping(defaultdict(<class 'int'>, {}))

dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_1_test_valid_input_defaultdict.py:9: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_mapping_1_test_valid_input_defaultdict.py::test_valid_input_defaultdict
============================== 1 failed in 0.03s ===============================
"""