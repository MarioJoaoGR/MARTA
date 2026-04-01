
import pytest
from flutes.io import _ReverseReadlineFile

@pytest.fixture
def reverse_readline():
    # Create a mock file-like object and generator function for testing
    class MockFile:
        def __init__(self, data):
            self.data = data
        
        def read(self, size=-1):
            if size == -1:
                return self.data
            else:
                return self.data[:size]
        
        def write(self, data):
            raise NotImplementedError("This method should not be called in the test")
    
    def mock_gen(data):
        yield from reversed(data.splitlines())
    
    fp = MockFile("line1\nline2\nline3\n")
    gen = mock_gen("line1\nline2\nline3\n")
    return _ReverseReadlineFile(fp, gen)

def test_edge_case(reverse_readline):
    lines = []
    for line in reverse_readline:
        lines.append(line.strip())
    
    assert lines == ['line3', 'line2', 'line1']
