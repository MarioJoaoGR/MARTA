
import logging
from flutes.log import _remove_handlers

@pytest.mark.parametrize("input_value", [None])
def test_none_input(input_value):
    with pytest.raises(TypeError):
        _remove_handlers(input_value)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log__remove_handlers_1_test_none_input
flutes/Test4DT_tests/test_flutes_log__remove_handlers_1_test_none_input.py:5:1: E0602: Undefined variable 'pytest' (undefined-variable)
flutes/Test4DT_tests/test_flutes_log__remove_handlers_1_test_none_input.py:7:9: E0602: Undefined variable 'pytest' (undefined-variable)


"""