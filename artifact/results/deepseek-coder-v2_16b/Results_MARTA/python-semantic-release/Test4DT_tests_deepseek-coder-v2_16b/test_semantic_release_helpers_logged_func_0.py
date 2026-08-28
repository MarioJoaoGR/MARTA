
import pytest
from semantic_release.helpers import LoggedFunction
import logging

# Set up a logger for testing
log = logging.getLogger(__name__)
logged_function = LoggedFunction(log)

def format_arg(arg):
    if isinstance(arg, str):
        return f"'{arg}'"
    return arg

@pytest.fixture
def setup_logger():
    logger = logging.getLogger(__name__)
    yield logger
    # Teardown code if needed

def test_logged_function_with_class_method(setup_logger):
    class MyClass:
        def __init__(self):
            self.logger = setup_logger
        
        @logged_function
        def my_method(self, arg1, arg2=None):
            return f"arg1={arg1}, arg2={arg2}"
    
    instance = MyClass()
    result = instance.my_method('value1', arg2='value2')
    assert result == "arg1=value1, arg2=value2"

def test_logged_function_with_standalone_function(setup_logger):
    @logged_function
    def standalone_function(arg1, arg2=None):
        return f"arg1={arg1}, arg2={arg2}"
    
    result = standalone_function('value1', arg2='value2')
    assert result == "arg1=value1, arg2=value2"
