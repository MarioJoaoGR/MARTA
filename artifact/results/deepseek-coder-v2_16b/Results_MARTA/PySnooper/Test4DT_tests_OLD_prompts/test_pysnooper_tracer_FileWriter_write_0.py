
import pytest
from pysnooper import tracer
import os

# Test scenario 1: Writing a string to a text file with default mode ('w') and encoding ('utf-8')
def test_write_to_file_string():
    path = 'test_example.txt'
    data = 'Hello, world!'
    
    tracer.FileWriter(path, True).write(data)
    
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    assert content == data
    os.remove(path)  # Clean up the test file

# Test scenario 2: Writing binary data to a binary file using ('wb') mode

# Test scenario 3: Appending data to an existing text file (overwrite=False)
def test_write_to_file_append():
    path = 'test_example.txt'
    with open(path, 'w') as f:
        pass  # Ensure the file exists and is empty if overwrite is False
    
    initial_data = 'Initial text.'
    tracer.FileWriter(path, False).write(initial_data)
    
    appended_data = 'Appended text.'
    tracer.FileWriter(path, False).write(appended_data)
    
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    assert content == initial_data + appended_data
    os.remove(path)  # Clean up the test file