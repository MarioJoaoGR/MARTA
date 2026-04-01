
import multiprocessing as mp
from pathlib import Path
import pytest
from flutes.multiproc import MultiprocessingFileWriter

def test_valid_inputs():
    queue = mp.Queue()
    writer = MultiprocessingFileWriter(Path('test_file'), 'r+')  # Open in read-write mode

    def write_to_queue():
        for i in range(5):
            queue.put(f'Message {i}')

    process = mp.Process(target=write_to_queue)
    process.start()

    # Give some time for the process to complete (assuming it runs quickly)
    import time
    time.sleep(1)

    writer._file.seek(0, 0)  # Move file pointer to the beginning
    content = writer._file.read()
    
    assert "Message" in content

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___init___1_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        queue = mp.Queue()
        writer = MultiprocessingFileWriter(Path('test_file'), 'r+')  # Open in read-write mode
    
        def write_to_queue():
            for i in range(5):
                queue.put(f'Message {i}')
    
        process = mp.Process(target=write_to_queue)
        process.start()
    
        # Give some time for the process to complete (assuming it runs quickly)
        import time
        time.sleep(1)
    
        writer._file.seek(0, 0)  # Move file pointer to the beginning
        content = writer._file.read()
    
>       assert "Message" in content
E       AssertionError: assert 'Message' in ''

flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___init___1_test_valid_inputs.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_multiproc_MultiprocessingFileWriter___init___1_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 1.10s ===============================

"""