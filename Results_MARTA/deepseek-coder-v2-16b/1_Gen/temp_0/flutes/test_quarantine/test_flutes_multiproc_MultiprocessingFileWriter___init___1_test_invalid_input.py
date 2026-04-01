
import pytest
from pathlib import Path
from multiprocessing_file_writer import MultiprocessingFileWriter

def test_invalid_input():
    # Test that an exception is raised when initializing with None as the path argument
    with pytest.raises(TypeError):
        MultiprocessingFileWriter(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter___init___1_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___init___1_test_invalid_input.py:4:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""