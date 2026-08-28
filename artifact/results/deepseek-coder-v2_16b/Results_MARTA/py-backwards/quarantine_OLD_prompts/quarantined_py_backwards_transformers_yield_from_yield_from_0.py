
import pytest
from unittest.mock import patch
from py_backwards.transformers.yield_from import yield_from

def simple_generator():
    yield 1
    yield 2
    yield 3

def faulty_generator():
    yield "a"
    yield "b"
    raise ValueError("Test error")

@pytest.mark.parametrize("generator, exc, assignment, expected", [
    (simple_generator(), StopIteration, [4, 5], [1, 2, 3, 4, 5])
])
def test_valid_inputs(generator, exc, assignment, expected):
    with patch('py_backwards.transformers.yield_from.iter', return_value=iter(generator)):
        result = list(yield_from(generator, exc, assignment))
        assert result == expected

@pytest.mark.parametrize("generator, exc, assignment", [
    (faulty_generator(), ValueError, 'assignment'),
    (simple_generator(), KeyError, [4, 5])
])
def test_invalid_inputs(generator, exc, assignment):
    with pytest.raises(exc):
        yield_from(generator, exc, assignment)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_yield_from_yield_from_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
___ test_valid_inputs[simple_generator-StopIteration-assignment0-expected0] ____

generator = <generator object simple_generator at 0x7f097902edc0>
exc = <class 'StopIteration'>, assignment = [4, 5], expected = [1, 2, 3, 4, 5]

    @pytest.mark.parametrize("generator, exc, assignment, expected", [
        (simple_generator(), StopIteration, [4, 5], [1, 2, 3, 4, 5])
    ])
    def test_valid_inputs(generator, exc, assignment, expected):
        with patch('py_backwards.transformers.yield_from.iter', return_value=iter(generator)):
>           result = list(yield_from(generator, exc, assignment))
E           TypeError: 'snippet' object is not callable

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_yield_from_yield_from_0.py:21: TypeError
_________ test_invalid_inputs[faulty_generator-ValueError-assignment] __________

generator = <generator object faulty_generator at 0x7f097902ee30>
exc = <class 'ValueError'>, assignment = 'assignment'

    @pytest.mark.parametrize("generator, exc, assignment", [
        (faulty_generator(), ValueError, 'assignment'),
        (simple_generator(), KeyError, [4, 5])
    ])
    def test_invalid_inputs(generator, exc, assignment):
        with pytest.raises(exc):
>           yield_from(generator, exc, assignment)
E           TypeError: 'snippet' object is not callable

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_yield_from_yield_from_0.py:30: TypeError
__________ test_invalid_inputs[simple_generator-KeyError-assignment1] __________

generator = <generator object simple_generator at 0x7f097902eea0>
exc = <class 'KeyError'>, assignment = [4, 5]

    @pytest.mark.parametrize("generator, exc, assignment", [
        (faulty_generator(), ValueError, 'assignment'),
        (simple_generator(), KeyError, [4, 5])
    ])
    def test_invalid_inputs(generator, exc, assignment):
        with pytest.raises(exc):
>           yield_from(generator, exc, assignment)
E           TypeError: 'snippet' object is not callable

/opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_yield_from_yield_from_0.py:30: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_yield_from_yield_from_0.py::test_valid_inputs[simple_generator-StopIteration-assignment0-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_yield_from_yield_from_0.py::test_invalid_inputs[faulty_generator-ValueError-assignment]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/py-backwards/Test4DT_tests_deepseek-coder-v2_16b/test_py_backwards_transformers_yield_from_yield_from_0.py::test_invalid_inputs[simple_generator-KeyError-assignment1]
============================== 3 failed in 0.07s ===============================
"""