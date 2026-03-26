
import pytest
from flutes.iterator import scanl

@pytest.mark.parametrize("func, iterable, initial, expected", [
    (lambda x, y: x + y, [1, 2, 3, 4], 0, [0, 1, 3, 6, 10]),
    (lambda x, y: x * y, [1, 2, 3, 4], 1, [1, 1, 2, 6, 24]),
    (lambda x, y: x - y, [5, 4, 3, 2], 0, [0, 5, 1, -2, -4])
])
def test_valid_inputs(func, iterable, initial, expected):
    result = list(scanl(func, iterable, initial))
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
collected 3 items

flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_valid_inputs.py . [ 33%]
.F                                                                       [100%]

=================================== FAILURES ===================================
______________ test_valid_inputs[<lambda>-iterable2-0-expected2] _______________

func = <function <lambda> at 0x7fea9403be20>, iterable = [5, 4, 3, 2]
initial = 0, expected = [0, 5, 1, -2, -4]

    @pytest.mark.parametrize("func, iterable, initial, expected", [
        (lambda x, y: x + y, [1, 2, 3, 4], 0, [0, 1, 3, 6, 10]),
        (lambda x, y: x * y, [1, 2, 3, 4], 1, [1, 1, 2, 6, 24]),
        (lambda x, y: x - y, [5, 4, 3, 2], 0, [0, 5, 1, -2, -4])
    ])
    def test_valid_inputs(func, iterable, initial, expected):
        result = list(scanl(func, iterable, initial))
>       assert result == expected
E       assert [0, -5, -9, -12, -14] == [0, 5, 1, -2, -4]
E         
E         At index 1 diff: -5 != 5
E         Use -v to get more diff

flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_valid_inputs.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_iterator_scanl_2_test_valid_inputs.py::test_valid_inputs[<lambda>-iterable2-0-expected2]
========================= 1 failed, 2 passed in 0.12s ==========================
"""