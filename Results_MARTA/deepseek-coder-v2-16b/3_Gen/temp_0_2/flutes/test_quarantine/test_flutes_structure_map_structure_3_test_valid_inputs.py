
import pytest
from flutes.structure import map_structure

# Assuming the test data is defined somewhere above this function
test_data = [
    ([1, 2, 3],),
    (['foo', 'bar'],)
]

@pytest.mark.parametrize("input_obj", test_data)
def test_valid_inputs(input_obj):
    expected = input_obj[0] if isinstance(input_obj[0], list) else {k: v ** 2 for k, v in input_obj[0].items()}
    result = map_structure(lambda x: x**2 if isinstance(x, (int, float)) else x, input_obj[0])
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py F [ 50%]
.                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_valid_inputs[input_obj0] _________________________

input_obj = ([1, 2, 3],)

    @pytest.mark.parametrize("input_obj", test_data)
    def test_valid_inputs(input_obj):
        expected = input_obj[0] if isinstance(input_obj[0], list) else {k: v ** 2 for k, v in input_obj[0].items()}
        result = map_structure(lambda x: x**2 if isinstance(x, (int, float)) else x, input_obj[0])
>       assert result == expected
E       assert [1, 4, 9] == [1, 2, 3]
E         
E         At index 1 diff: 4 != 2
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_structure_map_structure_3_test_valid_inputs.py::test_valid_inputs[input_obj0]
========================= 1 failed, 1 passed in 0.10s ==========================
"""