
import pytest
from pathlib import Path
from multiprocessing_file_writer import MultiprocessingFileWriter

@pytest.fixture
def setup_writer():
    return MultiprocessingFileWriter(Path('test.log'))

def test_enter_context(setup_writer):
    with pytest.raises(RuntimeError) as excinfo:
        with setup_writer as file:
            assert isinstance(file, file.__class__)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_multiproc_MultiprocessingFileWriter___enter___0_test_edge_case
flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___enter___0_test_edge_case.py:4:0: E0401: Unable to import 'multiprocessing_file_writer' (import-error)


"""