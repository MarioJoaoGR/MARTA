
import pytest
from string_utils.generation import generate

@pytest.fixture(params=[1, 2, 3, 4, 5])
def start(request):
    return request.param

@pytest.fixture(params=[6, 7, 8, 9, 10])
def stop(request):
    return request.param

@pytest.fixture(params=[1, 2, 3, 4, 5])
def step(request):
    return request.param

def test_generate(start, stop, step):
    roman_numerals = list(generate(start, stop, step))
    expected_numerals = [f"{i}" for i in range(start, stop, step)]
    assert roman_numerals == expected_numerals

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_string_utils_generation_generate_0_test_edge_cases
python-string-utils/Test4DT_tests/test_string_utils_generation_generate_0_test_edge_cases.py:3:0: E0611: No name 'generate' in module 'string_utils.generation' (no-name-in-module)


"""