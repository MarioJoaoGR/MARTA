
import pytest
from pathlib import Path
import multiprocessing
import threading
import time

# Assuming the class is in a module named 'flutes.multiproc'
from flutes.multiproc import MultiprocessingFileWriter

def write_to_file(path):
    with MultiprocessingFileWriter(path) as f:
        for i in range(10):  # Writing multiple lines to simulate multiple processes
            f.write(f"Process {multiprocessing.current_process().name}: Line {i}\n")

def test_valid_case():
    path = "testfile.log"
    num_processes = 4  # Number of processes to run concurrently
    
    # Create a multiprocessing environment where each process writes to the same file
    with multiprocessing.Manager() as manager:
        queue = manager.list()  # A shared list to collect results from all processes
        
        jobs = []
        for _ in range(num_processes):
            p = multiprocessing.Process(target=write_to_file, args=(path,))
            p.start()
            jobs.append(p)
        
        # Wait for all processes to complete
        for job in jobs:
            job.join()
        
        # Read the file and check its contents
        with open(path, 'r') as f:
            content = f.readlines()
        
        assert len(content) > 0, "File should have some content"
        for i in range(num_processes * 10):  # Each process writes 10 lines
            expected_line = f"Process {multiprocessing.current_process().name}: Line {i}\n"
            assert expected_line in content, f"Expected line '{expected_line}' not found in file"
        
        # Clean up the test file
        Path(path).unlink()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""