
import pytest
from pathlib import Path
from flutes.log import set_log_file, LOGGER
from logging.handlers import MultiprocessingFileHandler

def test_invalid_inputs():
    with pytest.raises(TypeError):
        set_log_file("invalid/path")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_log_set_log_file_1_test_invalid_inputs
flutes/Test4DT_tests/test_flutes_log_set_log_file_1_test_invalid_inputs.py:5:0: E0611: No name 'MultiprocessingFileHandler' in module 'logging.handlers' (no-name-in-module)


"""