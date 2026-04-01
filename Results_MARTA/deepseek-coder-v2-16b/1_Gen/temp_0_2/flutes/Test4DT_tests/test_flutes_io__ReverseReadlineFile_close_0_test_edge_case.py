
import io
from flutes.io import _ReverseReadlineFile  # Assuming the namespace is flutes.io
import pytest

# Mock data for testing
mock_data = "Line1\nLine2\nLine3\n"

@pytest.fixture
def setup_reverse_readline():
    fp = io.StringIO(mock_data)
    gen = (line.encode() for line in reversed(mock_data.splitlines()))
    return _ReverseReadlineFile(fp, gen)

def test_reverse_readline_read(setup_reverse_readline):
    rev_file = setup_reverse_readline
    assert rev_file.readline().decode().strip() == "Line3"
    assert rev_file.readline().decode().strip() == "Line2"
    assert rev_file.readline().decode().strip() == "Line1"

def test_reverse_readline_close(setup_reverse_readline):
    rev_file = setup_reverse_readline
    rev_file.close()
    # Additional assertions or checks can be added here to ensure the file is properly closed
