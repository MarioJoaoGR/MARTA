
import logging
from flutes.log import _remove_handlers

@pytest.mark.parametrize("logger", [None], indirect=True)
def test_none_input(logger):
    # Arrange
    logger = logging.getLogger('my_logger')
    
    # Act
    _remove_handlers(logger)
    
    # Assert
    assert len(logger.handlers) == 0, "Expected no handlers to be left after removing them"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log__remove_handlers_1_test_none_input
flutes/Test4DT_tests/test_flutes_log__remove_handlers_1_test_none_input.py:5:1: E0602: Undefined variable 'pytest' (undefined-variable)


"""