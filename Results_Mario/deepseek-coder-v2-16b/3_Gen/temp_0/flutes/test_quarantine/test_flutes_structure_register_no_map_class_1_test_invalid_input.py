
import pytest
from flutes.structure import register_no_map_class, _NO_MAP_TYPES

@pytest.mark.parametrize("invalid_type", [1, "string", None, int, float])
def test_register_no_map_class_invalid_input(invalid_type):
    with pytest.raises(TypeError):
        register_no_map_class(invalid_type)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 5 items

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
_________________ test_register_no_map_class_invalid_input[1] __________________

invalid_type = 1

    @pytest.mark.parametrize("invalid_type", [1, "string", None, int, float])
    def test_register_no_map_class_invalid_input(invalid_type):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py:7: Failed
_______________ test_register_no_map_class_invalid_input[string] _______________

invalid_type = 'string'

    @pytest.mark.parametrize("invalid_type", [1, "string", None, int, float])
    def test_register_no_map_class_invalid_input(invalid_type):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py:7: Failed
________________ test_register_no_map_class_invalid_input[None] ________________

invalid_type = None

    @pytest.mark.parametrize("invalid_type", [1, "string", None, int, float])
    def test_register_no_map_class_invalid_input(invalid_type):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py:7: Failed
________________ test_register_no_map_class_invalid_input[int] _________________

invalid_type = <class 'int'>

    @pytest.mark.parametrize("invalid_type", [1, "string", None, int, float])
    def test_register_no_map_class_invalid_input(invalid_type):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py:7: Failed
_______________ test_register_no_map_class_invalid_input[float] ________________

invalid_type = <class 'float'>

    @pytest.mark.parametrize("invalid_type", [1, "string", None, int, float])
    def test_register_no_map_class_invalid_input(invalid_type):
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py::test_register_no_map_class_invalid_input[1]
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py::test_register_no_map_class_invalid_input[string]
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py::test_register_no_map_class_invalid_input[None]
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py::test_register_no_map_class_invalid_input[int]
FAILED flutes/Test4DT_tests/test_flutes_structure_register_no_map_class_1_test_invalid_input.py::test_register_no_map_class_invalid_input[float]
============================== 5 failed in 0.09s ===============================

"""