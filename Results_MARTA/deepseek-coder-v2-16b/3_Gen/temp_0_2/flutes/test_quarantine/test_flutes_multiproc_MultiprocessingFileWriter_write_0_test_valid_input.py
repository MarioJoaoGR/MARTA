
import pytest
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture
def writer():
    return MultiprocessingFileWriter('test_output.log')

def test_valid_input(writer):
    message = "Test message"
    writer.write(message)  # Write a valid input to the file

    with open('test_output.log', 'r') as f:
        content = f.read()
        assert message in content, "The written message is not found in the file content."

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

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

writer = <flutes.multiproc.MultiprocessingFileWriter object at 0x7f4c64ea6190>

    def test_valid_input(writer):
        message = "Test message"
        writer.write(message)  # Write a valid input to the file
    
        with open('test_output.log', 'r') as f:
            content = f.read()
>           assert message in content, "The written message is not found in the file content."
E           AssertionError: The written message is not found in the file content.
E           assert 'Test message' in ''

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0_test_valid_input.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_0_test_valid_input.py::test_valid_input
============================== 1 failed in 0.10s ===============================
"""