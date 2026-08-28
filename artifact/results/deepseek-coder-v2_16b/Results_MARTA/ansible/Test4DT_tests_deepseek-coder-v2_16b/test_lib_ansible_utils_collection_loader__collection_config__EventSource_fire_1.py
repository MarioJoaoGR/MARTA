
import pytest
from _EventSource import _EventSource

# Test Scenario 1: Test standard input with valid handler functions
def test_valid_input():
    event_source = _EventSource()
    handle1 = lambda: print('Handler 1')
    handle2 = lambda: print('Handler 2')
    event_source.add_handler(handle1)
    event_source.add_handler(handle2)
    
    # Capture the output of the handlers
    captured_output = []
    def capture_output(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            captured_output.append(result)
            return result
        return wrapper
    
    # Apply the capture function to each handler
    handle1_capture = capture_output(handle1)
    handle2_capture = capture_output(handle2)
    
    event_source._handlers = {handle1_capture, handle2_capture}
    event_source.trigger_event()
    
    # Check that both handlers were called and output was captured
    assert len(captured_output) == 2
    assert all(isinstance(item, str) for item in captured_output)
    assert 'Handler 1' in captured_output[0]
    assert 'Handler 2' in captured_output[1]

# Test Scenario 2: Test with None input to check error handling
def test_edge_case():
    event_source = _EventSource()
    handle = lambda: print('Handler 1')
    event_source.add_handler(handle)
    
    # Trigger the event with None input, which should raise a TypeError
    with pytest.raises(TypeError):
        event_source.fire(None)

# Test Scenario 3: Test with invalid input type to check error handling
def test_invalid_input():
    event_source = _EventSource()
    handle = lambda: print('Handler 1')
    event_source.add_handler(handle)
    
    # Trigger the event with an invalid input type, which should raise a TypeError
    with pytest.raises(TypeError):
        event_source.fire('invalid')
