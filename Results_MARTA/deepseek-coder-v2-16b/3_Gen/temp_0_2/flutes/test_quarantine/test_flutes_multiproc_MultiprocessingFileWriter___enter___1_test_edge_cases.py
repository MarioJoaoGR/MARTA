
import pytest
from flutes.multiproc import MultiprocessingFileWriter
from pathlib import Path
import multiprocessing as mp
import threading
from typing import IO, Any

@pytest.fixture
def setup_writer():
    return MultiprocessingFileWriter(Path('testfile.log'))

def test_enter_context(setup_writer):
    writer = setup_writer
    with pytest.raises(NotImplementedError):  # Since __enter__ should be a stub, it raises an error by default
        assert isinstance(writer.__enter__(), IO)

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

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___enter___1_test_edge_cases.py F [100%]

=================================== FAILURES ===================================
______________________________ test_enter_context ______________________________

setup_writer = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f591f657b50>

    def test_enter_context(setup_writer):
        writer = setup_writer
        with pytest.raises(NotImplementedError):  # Since __enter__ should be a stub, it raises an error by default
>           assert isinstance(writer.__enter__(), IO)
E           AssertionError: assert False
E            +  where False = isinstance(<_io.TextIOWrapper name='testfile.log' mode='a' encoding='utf-8'>, IO)
E            +    where <_io.TextIOWrapper name='testfile.log' mode='a' encoding='utf-8'> = __enter__()
E            +      where __enter__ = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f591f657b50>.__enter__

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___enter___1_test_edge_cases.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___enter___1_test_edge_cases.py::test_enter_context
============================== 1 failed in 0.10s ===============================
"""