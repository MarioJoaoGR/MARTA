
import pytest
from flutes.exception import _handle_exception

def test_invalid_input():
    def simple_generator():
        yield 1
        yield 2
        yield 3

    gen = simple_generator()
    with pytest.raises(Exception) as exc_info:
        for value in _captured_generator(gen, (), {}):
            if value == 2:
                raise Exception("Test exception")
    assert str(exc_info.value) == "Test exception"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_exception__captured_generator_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_exception__captured_generator_0_test_invalid_input.py:3:0: E0611: No name '_handle_exception' in module 'flutes.exception' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_exception__captured_generator_0_test_invalid_input.py:13:21: E0602: Undefined variable '_captured_generator' (undefined-variable)


"""