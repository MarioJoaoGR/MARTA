
import pytest
from ansible.plugins.connection.psrp import Connection

# Test initialization of the Connection class with default parameters
def test_default_init():
    conn = Connection(host='remote_host')
    assert conn.always_pipeline_modules is True
    assert conn.has_native_async is True
    assert conn.runspace is None
    assert conn.host == 'remote_host'
    assert conn._last_pipeline is False
    assert conn._shell_type == 'powershell'

# Test initialization of the Connection class with custom parameters
def test_custom_init():
    conn = Connection(host='another_host', always_pipeline_modules=False, has_native_async=False)
    assert conn.always_pipeline_modules is False
    assert conn.has_native_async is False
    assert conn.runspace is None
    assert conn.host == 'another_host'
    assert conn._last_pipeline is False
    assert conn._shell_type == 'powershell'

# Test parsing pipeline result with no errors
def test_parse_pipeline_result_no_errors():
    # Assuming pipeline is an instance of a class that contains its own rc, stdout, and stderr attributes
    pipeline = DummyPipeline(output=[b"line1", b"line2"], had_errors=False)
    conn = Connection()
    result = conn._parse_pipeline_result(pipeline)
    assert result[0] == 0
    assert result[1].decode('utf-8') == "line1\nline2"
    assert result[2] == b""

# Test parsing pipeline result with errors
def test_parse_pipeline_result_with_errors():
    # Assuming pipeline is an instance of a class that contains its own rc, stdout, and stderr attributes
    pipeline = DummyPipeline(output=[b"line1", b"line2"], had_errors=True)
    conn = Connection()
    result = conn._parse_pipeline_result(pipeline)
    assert result[0] == 1
    assert result[1].decode('utf-8') == "line1\nline2"
    assert result[2].decode('utf-8') == ""

# Dummy class to simulate pipeline for testing purposes
class DummyPipeline:
    def __init__(self, output, had_errors):
        self.output = output
        self.had_errors = had_errors
