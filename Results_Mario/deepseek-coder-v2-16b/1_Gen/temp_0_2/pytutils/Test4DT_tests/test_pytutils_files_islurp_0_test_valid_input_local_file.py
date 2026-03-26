
import os
import sys
import tempfile
import pytest
from pytutils.files import islurp

@pytest.fixture(scope="module")
def temp_file():
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as f:
        lines = ["line1\n", "line2\n", "line3\n"]
        f.writelines(lines)
        f.seek(0)
        yield f.name
    os.unlink(f.name)

def test_valid_input_local_file(temp_file):
    with open(temp_file, 'r') as file:
        lines = list(islurp(temp_file))
        assert lines == ["line1\n", "line2\n", "line3\n"]
