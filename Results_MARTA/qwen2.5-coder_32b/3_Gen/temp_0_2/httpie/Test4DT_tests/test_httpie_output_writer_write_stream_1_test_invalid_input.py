
import pytest
from unittest.mock import patch
from httpie.output.writer import write_stream
from io import StringIO

def test_invalid_input():
    with pytest.raises(TypeError):
        stream = 'not iterable'
        outfile = open('temp_output.txt', 'w')
        with patch('httpie.output.writer.write_stream'):
            write_stream(stream, outfile, True)
