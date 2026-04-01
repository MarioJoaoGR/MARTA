
import pytest
from flutes.structure import register_no_map_class, _NO_MAP_TYPES
from unittest.mock import patch

@pytest.mark.parametrize("container_type", [list, dict])
def test_none_input(container_type):
    with patch('flutes.structure._NO_MAP_TYPES', set()):
        register_no_map_class(container_type)
        assert container_type in _NO_MAP_TYPES

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_none_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_none_input[list] _____________________________

container_type = <class 'list'>

    @pytest.mark.parametrize("container_type", [list, dict])
    def test_none_input(container_type):
        with patch('flutes.structure._NO_MAP_TYPES', set()):
            register_no_map_class(container_type)
>           assert container_type in _NO_MAP_TYPES
E           AssertionError: assert <class 'list'> in set()

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_none_input.py:10: AssertionError
____________________________ test_none_input[dict] _____________________________

container_type = <class 'dict'>

    @pytest.mark.parametrize("container_type", [list, dict])
    def test_none_input(container_type):
        with patch('flutes.structure._NO_MAP_TYPES', set()):
            register_no_map_class(container_type)
>           assert container_type in _NO_MAP_TYPES
E           AssertionError: assert <class 'dict'> in set()

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_none_input.py:10: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_none_input.py::test_none_input[list]
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_0_test_none_input.py::test_none_input[dict]
============================== 2 failed in 0.12s ===============================
"""