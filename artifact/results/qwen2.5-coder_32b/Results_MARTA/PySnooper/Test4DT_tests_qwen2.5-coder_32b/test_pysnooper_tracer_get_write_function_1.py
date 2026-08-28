
import sys
import pytest
from pysnooper.tracer import get_write_function




def test_write_with_custom_callable():
    captured_output = []
    
    def custom_writer(s):
        captured_output.append(s)
    
    write_func = get_write_function(custom_writer, False)
    write_func('This will be handled by the custom writer.\n')
    
    assert captured_output == ['This will be handled by the custom writer.\n']

def test_write_with_writable_stream():
    class ConsoleWriter:
        def __init__(self):
            self.output = []
        
        def write(self, s):
            self.output.append(s)
    
    console_writer = ConsoleWriter()
    write_func = get_write_function(console_writer, False)
    write_func('This will be handled by the console writer.\n')
    
    assert console_writer.output == ['This will be handled by the console writer.\n']