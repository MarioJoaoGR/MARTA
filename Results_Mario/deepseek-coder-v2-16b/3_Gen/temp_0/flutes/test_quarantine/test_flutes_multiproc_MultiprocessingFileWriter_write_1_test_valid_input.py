
import pytest
from pathlib import Path
from flutes.multiproc import MultiprocessingFileWriter

@pytest.fixture(scope="function")
def writer():
    # Create a temporary file for testing
    temp_file = Path('test_output.log')
    yield MultiprocessingFileWriter(temp_file)
    # Clean up the temporary file after the test
    if temp_file.exists():
        temp_file.unlink()

def test_valid_input(writer):
    message = "This is a valid input message."
    writer.write(message)  # Write the message to the file

    # Read and check if the message was written correctly
    with open('test_output.log', 'r') as f:
        content = f.read()
    assert message in content, "The written message does not match the expected input."

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

writer = <flutes.multiproc.MultiprocessingFileWriter object at 0x7fef55b0dfd0>

    def test_valid_input(writer):
        message = "This is a valid input message."
        writer.write(message)  # Write the message to the file
    
        # Read and check if the message was written correctly
        with open('test_output.log', 'r') as f:
            content = f.read()
>       assert message in content, "The written message does not match the expected input."
E       AssertionError: The written message does not match the expected input.
E       assert 'This is a valid input message.' in ''

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_1_test_valid_input.py:22: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter_write_1_test_valid_input.py::test_valid_input
============================== 1 failed in 0.11s ===============================
"""