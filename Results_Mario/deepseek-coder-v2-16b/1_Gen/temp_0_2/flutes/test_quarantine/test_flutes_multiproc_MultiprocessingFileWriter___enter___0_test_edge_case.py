
import pytest
from unittest.mock import patch, MagicMock
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture
def writer():
    return MultiprocessingFileWriter('dummy_path', 'a')

def test_enter(writer):
    with patch('flutes.multiproc.open', new_callable=MagicMock) as mock_file:
        # When the context manager is entered, it should return the file object itself
        assert writer.__enter__() == mock_file.return_value

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

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___enter___0_test_edge_case.py F [100%]

=================================== FAILURES ===================================
__________________________________ test_enter __________________________________

writer = <flutes.multiproc.MultiprocessingFileWriter object at 0x7fd6896e3650>

    def test_enter(writer):
        with patch('flutes.multiproc.open', new_callable=MagicMock) as mock_file:
            # When the context manager is entered, it should return the file object itself
>           assert writer.__enter__() == mock_file.return_value
E           AssertionError: assert <_io.TextIOWr...oding='utf-8'> == <MagicMock na...559393413008'>
E             
E             Use -v to get more diff

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___enter___0_test_edge_case.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___enter___0_test_edge_case.py::test_enter
============================== 1 failed in 0.10s ===============================
"""