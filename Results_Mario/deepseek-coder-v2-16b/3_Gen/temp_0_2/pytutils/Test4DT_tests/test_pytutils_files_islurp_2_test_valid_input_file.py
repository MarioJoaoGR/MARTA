
import pytest
import sys
import os
import functools
from pytutils.files import islurp

# Mocking sys.stdin for testing purposes
class StringIO:
    def __init__(self, string=''):
        self.string = string
        self.index = 0

    def read(self, size=None):
        if size is None or self.index >= len(self.string):
            return ''
        result = self.string[self.index:]
        self.index = min(len(self.string), self.index + (size or 1))
        return result

    def readline(self, size=None):
        if self.index >= len(self.string):
            return ''
        end_index = self.index + (size or 1)
        result = self.string[self.index:end_index]
        self.index = min(len(self.string), end_index)
        return result

def test_valid_input_file():
    # Create a temporary file with some content
    temp_file_path = 'temp_test_file.txt'
    with open(temp_file_path, 'w') as f:
        f.write("Line 1\nLine 2\nLine 3")

    # Test reading from the temporary file
    lines = []
    for line in islurp(temp_file_path):
        lines.append(line)
    
    assert lines == ['Line 1\n', 'Line 2\n', 'Line 3']

    # Clean up the temporary file
    os.remove(temp_file_path)
