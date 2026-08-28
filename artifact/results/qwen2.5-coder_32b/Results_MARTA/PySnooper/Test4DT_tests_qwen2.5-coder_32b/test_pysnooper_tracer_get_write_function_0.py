
import sys
import os
from io import StringIO
from pysnooper.tracer import get_write_function

# Test writing to standard error
def test_get_write_function_stderr():
    original_stderr = sys.stderr
    try:
        sys.stderr = captured_output = StringIO()
        write_func = get_write_function(None, False)
        write_func('This will be written to stderr.\n')
        assert captured_output.getvalue() == 'This will be written to stderr.\n'
    finally:
        sys.stderr = original_stderr

# Test writing to a file with overwrite enabled
def test_get_write_function_file_overwrite():
    output_path = 'test_output.txt'
    try:
        write_func = get_write_function(output_path, True)
        write_func('This content will overwrite the file.\n')
        with open(output_path, 'r') as f:
            assert f.read() == 'This content will overwrite the file.\n'
    finally:
        os.remove(output_path)

# Test writing to a file with overwrite disabled (append mode)
def test_get_write_function_file_append():
    output_path = 'test_output.txt'
    try:
        write_func = get_write_function(output_path, True)
        write_func('Initial content.\n')
        write_func = get_write_function(output_path, False)
        write_func('Appended content.\n')
        with open(output_path, 'r') as f:
            assert f.read() == 'Initial content.\nAppended content.\n'
    finally:
        os.remove(output_path)

# Test using a custom callable as the write function
def test_get_write_function_custom_callable():
    captured_output = []
    def custom_writer(s):
        captured_output.append(s)
    write_func = get_write_function(custom_writer, False)
    write_func('This will be handled by the custom writer.\n')
    assert captured_output == ['This will be handled by the custom writer.\n']

# Test using an instance of WritableStream
def test_get_write_function_writable_stream():
    class ConsoleWriter:
        def __init__(self):
            self.output = []
        def write(self, s):
            self.output.append(s)
    console_writer = ConsoleWriter()
    write_func = get_write_function(console_writer, False)
    write_func('This will be handled by the console writer.\n')
    assert console_writer.output == ['This will be handled by the console writer.\n']
