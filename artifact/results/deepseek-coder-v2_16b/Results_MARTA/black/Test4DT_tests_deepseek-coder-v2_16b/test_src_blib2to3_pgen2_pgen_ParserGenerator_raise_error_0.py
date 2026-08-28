
import pytest
from pathlib import Path
from io import StringIO
from tokenize import generate_tokens
from blib2to3.pgen2.pgen import ParserGenerator


def test_invalid_file(tmpdir):
    filename = tmpdir / "nonexistent_file.py"
    with pytest.raises(FileNotFoundError):
        ParserGenerator(filename)

def test_missing_stream():
    with pytest.raises(FileNotFoundError):
        ParserGenerator("source_code.py")
