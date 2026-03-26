
# Module: flutes.io
import pytest
from io import StringIO
import os
from flutes.io import _ReverseReadlineFile

# Test initialization with a file-like object and a generator function
def test_reverse_readline_file():
    sample_data = "Line1\nLine2\nLine3\n"
    file_obj = StringIO(sample_data)
    
    def reverse_gen():
        yield "Line3"
        yield "Line2"
        yield "Line1"
    
    reverse_readline = _ReverseReadlineFile(fp=file_obj, gen=reverse_gen())
    
    assert reverse_readline.readline() == "Line3\n"
    assert reverse_readline.readline() == "Line2\n"
    assert reverse_readline.readline() == "Line1\n"

# Test initialization with a file-like object and a generator function using different encoding
def test_reverse_readline_file_with_encoding():
    sample_data = "Line1\nLine2\nLine3\n"
    file_obj = StringIO(sample_data)
    
    def reverse_gen():
        yield b'Line3'
        yield b'Line2'
        yield b'Line1'
    
    reverse_readline = _ReverseReadlineFile(fp=file_obj, gen=reverse_gen())
    
    assert reverse_readline.readline().decode('utf-8') == "Line3\n"
    assert reverse_readline.readline().decode('utf-8') == "Line2\n"
    assert reverse_readline.readline().decode('utf-8') == "Line1\n"

# Test initialization with a file-like object and a generator function using different encoding and allow_empty_lines=True
def test_reverse_readline_file_with_encoding_and_allow_empty_lines():
    sample_data = "Line1\nLine2\nLine3\n"
    file_obj = StringIO(sample_data)
    
    def reverse_gen():
        yield b'Line3'
        yield b'Line2'
        yield b'Line1'
    
    reverse_readline = _ReverseReadlineFile(fp=file_obj, gen=reverse_gen(), allow_empty_lines=True)
    
    assert reverse_readline.readline().decode('utf-8') == "Line3\n"
    assert reverse_readline.readline().decode('utf-8') == "Line2\n"
    assert reverse_readline.readline().decode('utf-8') == "Line1\n"

# Test generator function with a real file
def test_generator_function():
    file_path = 'test_file.txt'
    with open(file_path, 'w') as f:
        f.write("Line1\nLine2\nLine3\n")
    
    def generator(fp):
        fp.seek(0, os.SEEK_END)
        file_size = fp.tell()
        while file_size > 0:
            fp.seek(max(0, file_size - 8192))
            buffer = fp.read().decode('utf-8')
            lines = buffer.split('\n')
            for line in reversed(lines):
                if len(line) > 0:
                    yield line
            file_size -= 8192
    
    with open(file_path, 'rb') as fp:
        reverse_readline = _ReverseReadlineFile(fp=fp, gen=generator(fp))
        
        assert reverse_readline.readline() == "Line3\n"
        assert reverse_readline.readline() == "Line2\n"
        assert reverse_readline.readline() == "Line1\n"
    
    os.remove(file_path)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_io__ReverseReadlineFile_generator_0
flutes/Test4DT_tests/test_flutes_io__ReverseReadlineFile_generator_0.py:50:23: E1123: Unexpected keyword argument 'allow_empty_lines' in constructor call (unexpected-keyword-arg)


"""