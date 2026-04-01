
import pytest
from multiprocessing_file_writer import MultiprocessingFileWriter
import os

def test_edge_case():
    with pytest.raises(TypeError):
        writer = MultiprocessingFileWriter(None)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter___exit___0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___exit___0_test_edge_case.py:3:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""