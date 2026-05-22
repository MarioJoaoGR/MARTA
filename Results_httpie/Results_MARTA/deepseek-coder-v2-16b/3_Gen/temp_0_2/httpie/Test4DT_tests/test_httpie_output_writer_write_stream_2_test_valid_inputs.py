
import pytest
from io import StringIO
from httpie.output.writer import write_stream
from unittest.mock import patch

@pytest.fixture(autouse=True)
def setup():
    f = StringIO('This is a test string.')
    outfile = StringIO()
    return f, outfile

def test_valid_inputs(setup):
    f, outfile = setup
    with patch('sys.stdout', new=StringIO()) as mock_stdout:
        write_stream(f, outfile, True)
        assert outfile.getvalue() == 'This is a test string.'
        # Ensure stdout is flushed correctly if needed (not applicable here but good practice)
