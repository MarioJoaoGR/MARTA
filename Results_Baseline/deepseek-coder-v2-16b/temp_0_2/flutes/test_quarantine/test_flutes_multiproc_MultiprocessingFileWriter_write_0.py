
import pytest
from pathlib import Path
import threading
import multiprocessing as mp
from typing import Union as PathType

# Import the function from the module
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture
def setup_writer():
    # Create a temporary file for testing
    temp_file = Path('test_output.log')
    writer = MultiprocessingFileWriter(temp_file)
    yield writer
    # Clean up the temporary file after the test
    if temp_file.exists():
        temp_file.unlink()

def test_init_default_mode(setup_writer):
    writer = setup_writer
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0.py F [100%]

=================================== FAILURES ===================================
____________________________ test_init_default_mode ____________________________

setup_writer = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f8f9d9ab050>

    def test_init_default_mode(setup_writer):
        writer = setup_writer
>       assert isinstance(writer._file, Path), "File should be opened correctly"
E       AssertionError: File should be opened correctly
E       assert False
E        +  where False = isinstance(<_io.TextIOWrapper name='test_output.log' mode='a' encoding='utf-8'>, Path)
E        +    where <_io.TextIOWrapper name='test_output.log' mode='a' encoding='utf-8'> = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f8f9d9ab050>._file

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0.py:23: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0.py::test_init_default_mode
============================== 1 failed in 0.09s ===============================
"""