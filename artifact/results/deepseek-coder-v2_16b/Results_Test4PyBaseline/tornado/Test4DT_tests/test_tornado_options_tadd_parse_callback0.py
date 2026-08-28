
# Module: tornado.options
import pytest
from typing import Callable
from unittest.mock import patch
from tornado.options import add_parse_callback, OptionParser
try:  # Python 3.x
    from io import StringIO
except ImportError:  # Python 2.x
    from cStringIO import StringIO

# Mock the OptionParser class since it's not defined in this module
class MockOptionParser:
    def __init__(self):
        self._callbacks = []
    
    def add_parse_callback(self, callback):
        self._callbacks.append(callback)
    
    def parse_command_line(self, args=None):
        for callback in self._callbacks:
            callback()

# Patch the OptionParser import to use our mock class
@patch('tornado.options.OptionParser', MockOptionParser)
def test_add_parse_callback():
    # Define a simple callback function
    def print_options():
        print("Options parsed.")
    
    # Call the function with the callback
    add_parse_callback(print_options)
    
    # Create an instance of OptionParser and call parse_command_line to trigger callbacks
    options = MockOptionParser()
    options.parse_command_line(['--dummy-arg'])  # Dummy args for method signature
    
    # Capture the output of the print statement in the callback
    with patch('sys.stdout', new=StringIO()) as fake_out:
        print_options()  # This should call the registered callback
        assert fake_out.getvalue().strip() == "Options parsed."

# Test that multiple callbacks can be added and invoked correctly
def test_multiple_callbacks():
    def callback1():
        print("Callback 1 executed.")
    
    def callback2():
        print("Callback 2 executed.")
    
    add_parse_callback(callback1)
    add_parse_callback(callback2)
    
    options = MockOptionParser()
    options.parse_command_line(['--dummy-arg'])  # Dummy args for method signature
    
    with patch('sys.stdout', new=StringIO()) as fake_out:
        callback1()  # This should call the first registered callback
        assert fake_out.getvalue().strip() == "Callback 1 executed."
        
        options.parse_command_line(['--dummy-arg'])  # Trigger all callbacks again