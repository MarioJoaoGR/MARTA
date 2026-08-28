
import pytest
from httpie.output.streams import RawStream

# Test 1: Default Initialization with Default Chunk Size
def test_default_chunk_size():
    raw_stream = RawStream()
    data = raw_stream.read()
    assert len(data.split('\n')) == 1024, f"Expected 1024 lines but got {len(data.split('\n'))}"

# Test 2: Initialization with Specified Chunk Size
def test_specified_chunk_size():
    raw_stream = RawStream(chunk_size=512)
    data = raw_stream.read(3)
    assert len(data.split('\n')) == 3, f"Expected 3 lines but got {len(data.split('\n'))}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
SyntaxError: f-string expression part cannot include a backslash (line 9, col 97)
    assert len(data.split('\n')) == 1024, f"Expected 1024 lines but got {len(data.split('\n'))}"
"""