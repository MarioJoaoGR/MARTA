
import pytest
from pathlib import Path
from multiprocessing_file_writer import MultiprocessingFileWriter

def test_invalid_input():
    writer = MultiprocessingFileWriter(Path('output.log'))
    
    with pytest.raises(TypeError):
        writer.write(12345)  # Passing an integer, which should raise a TypeError

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter_write_1_test_invalid_input
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_1_test_invalid_input.py:4:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""