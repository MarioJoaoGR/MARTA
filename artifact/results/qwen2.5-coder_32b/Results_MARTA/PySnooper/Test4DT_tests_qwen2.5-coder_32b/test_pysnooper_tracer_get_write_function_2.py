
import sys
import pytest
from unittest.mock import patch
from pysnooper.tracer import get_write_function




def test_custom_callable():
    captured_output = []
    
    def custom_writer(s):
        captured_output.append(s)
    
    write_func = get_write_function(custom_writer, False)
    write_func('This will be handled by the custom writer.\n')
    assert captured_output == ['This will be handled by the custom writer.\n']

def test_writable_stream():
    class ConsoleWriter:
        def __init__(self):
            self.captured_output = []
        
        def write(self, s):
            self.captured_output.append(s)
    
    console_writer = ConsoleWriter()
    write_func = get_write_function(console_writer, False)
    write_func('This will be handled by the console writer.\n')
    assert console_writer.captured_output == ['This will be handled by the console writer.\n']