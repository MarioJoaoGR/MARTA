
import sys
import io
import pytest
from pytutils.files import islurp

@pytest.mark.skip(reason="This is an example of how to write a pytest function for testing stdin mode")
def test_stdin_mode():
    # Mock the input by redirecting sys.stdin
    mock_input = "Hello\nWorld\n"
    sys.stdin = io.StringIO(mock_input)
    
    # Call the islurp function with '-' to read from stdin
    lines = list(islurp('-', allow_stdin=True))
    
    # Assert that the output matches the mock input
    assert lines == ['Hello\n', 'World\n']
