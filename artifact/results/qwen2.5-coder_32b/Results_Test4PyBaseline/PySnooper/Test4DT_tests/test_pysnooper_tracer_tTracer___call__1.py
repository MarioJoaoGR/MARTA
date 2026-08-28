
import pytest
from pysnooper.tracer import Tracer, DISABLED
import inspect

# Mocking the _wrap_class and _wrap_function methods for testing purposes
def mock_wrap_class(self, cls):
    return f"Wrapped class: {cls.__name__}"

def mock_wrap_function(self, func):
    return f"Wrapped function: {func.__name__}"

@pytest.fixture(autouse=True)
def patch_wrappers(monkeypatch):
    monkeypatch.setattr('pysnooper.tracer.Tracer._wrap_class', mock_wrap_class)
    monkeypatch.setattr('pysnooper.tracer.Tracer._wrap_function', mock_wrap_function)

# Test case for when DISABLED is True
@pytest.mark.parametrize("disabled_value", [True, False])
def test_call_with_disabled(monkeypatch, disabled_value):
    tracer = Tracer()
    original_function = lambda x: x + 1
    original_class = type('TestClass', (object,), {'method': lambda self: None})
    
    # Patch the DISABLED variable to control its value
    monkeypatch.setattr('pysnooper.tracer.DISABLED', disabled_value)
    
    if disabled_value:
        assert tracer(original_function) is original_function