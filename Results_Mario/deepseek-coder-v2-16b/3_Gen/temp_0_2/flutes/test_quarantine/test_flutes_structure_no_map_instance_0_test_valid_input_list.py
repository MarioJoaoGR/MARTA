
import pytest
from flutes.structure import no_map_instance, _NO_MAP_INSTANCE_ATTR

def test_valid_input_list():
    my_list = [1, 2, 3]
    no_map_instance(my_list)
    assert hasattr(my_list, _NO_MAP_INSTANCE_ATTR), f"Expected {_NO_MAP_INSTANCE_ATTR} attribute to be set on the list."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_structure_no_map_instance_0_test_valid_input_list.py F [100%]

=================================== FAILURES ===================================
____________________________ test_valid_input_list _____________________________

    def test_valid_input_list():
        my_list = [1, 2, 3]
        no_map_instance(my_list)
>       assert hasattr(my_list, _NO_MAP_INSTANCE_ATTR), f"Expected {_NO_MAP_INSTANCE_ATTR} attribute to be set on the list."
E       AssertionError: Expected --no-map-- attribute to be set on the list.
E       assert False
E        +  where False = hasattr([1, 2, 3], '--no-map--')

flutes/Test4DT_tests/test_flutes_structure_no_map_instance_0_test_valid_input_list.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_no_map_instance_0_test_valid_input_list.py::test_valid_input_list
============================== 1 failed in 0.08s ===============================
"""