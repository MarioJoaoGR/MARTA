
import pytest
from collections import Counter
from your_module_name import _is_counter  # Replace 'your_module_name' with the actual module name where _is_counter is defined

def test_edge_case():
    assert not _is_counter(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_dataclasses_json_utils__is_counter_1_test_edge_case
dataclasses-json/Test4DT_tests/test_dataclasses_json_utils__is_counter_1_test_edge_case.py:4:0: E0401: Unable to import 'your_module_name' (import-error)


"""