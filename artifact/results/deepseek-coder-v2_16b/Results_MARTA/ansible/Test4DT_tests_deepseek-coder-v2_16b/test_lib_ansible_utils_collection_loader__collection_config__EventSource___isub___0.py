
import pytest
from unittest.mock import patch

class _EventSource:
    def __init__(self):
        self._handlers = set()

    def add_handler(self, handler):
        """
        Registers a new handler function to be called when events are triggered.
        
        Parameters:
            handler (callable): The function to be registered as an event handler.
        """
        self._handlers.add(handler)

    def remove_handler(self, handler):
        """
        Removes a previously registered handler function so it will no longer be called when events are triggered.
        
        Parameters:
            handler (callable): The function to be removed from the event handlers.
        """
        self._handlers.discard(handler)

    def trigger_event(self):
        """
        Calls all registered handler functions in the order they were added.
        
        This method iterates over the set of registered handlers and calls each one in the order they were added.
        """
        for handler in self._handlers:
            handler()

    def __isub__(self, handler):
        try:
            self._handlers.remove(handler)
        except KeyError:
            pass

        return self

# Test Scenario 1: test_valid_inputs
def test_valid_inputs():
    event_source = _EventSource()
    
    def handle1():
        print("Handler 1")

    def handle2():
        print("Handler 2")

    # Register handlers
    event_source.add_handler(handle1)
    event_source.add_handler(handle2)

    # Capture the output of trigger_event
    with patch('sys.stdout', new=StringIO()) as fake_output:
        event_source.trigger_event()
        assert fake_output.getvalue().strip() == 'Handler 1Handler 2'

# Test Scenario 2: test_edge_cases
def test_edge_cases():
    event_source = _EventSource()
    
    def handle1():
        print("Handler 1")

    def handle2():
        print("Handler 2")

    # Add and remove handlers with None, empty list, and boundary values
    event_source.add_handler(handle1)
    event_source.remove_handler(handle1)
    
    event_source.add_handler(None)
    event_source.remove_handler(None)
    
    event_source.add_handler(lambda: None)
    event_source.remove_handler(lambda: None)
    
    # Capture the output of trigger_event
    with patch('sys.stdout', new=StringIO()) as fake_output:
        event_source.trigger_event()
        assert fake_output.getvalue().strip() == ''

# Test Scenario 3: test_invalid_inputs
def test_invalid_inputs():
    event_source = _EventSource()
    
    def handle1():
        print("Handler 1")

    def handle2():
        print("Handler 2")

    # Add and remove handlers with invalid values to ensure error handling works correctly
    with pytest.raises(TypeError):
        event_source.add_handler(42)  # Adding an integer (invalid type)
    
    with pytest.raises(KeyError):
        event_source.remove_handler(lambda: None)  # Removing a non-existent handler
    
    # Capture the output of trigger_event
    with patch('sys.stdout', new=StringIO()) as fake_output:
        event_source.trigger_event()
        assert fake_output.getvalue().strip() == ''
