
import pytest
from pytutils.debug import interact
import inspect
import builtins

# Mock the input function to prevent it from being called during testing
def mock_input(prompt):
    return ""

@pytest.mark.parametrize("invalid_input", [None, 123, [], {}])
def test_invalid_inputs(monkeypatch, invalid_input):
    # Monkeypatch the input function to prevent it from being called
    monkeypatch.setattr(builtins, 'input', mock_input)
    
    with pytest.raises(TypeError):
        interact(banner=invalid_input)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
time exceeded
"""