
import pytest
from pathlib import Path
from io import StringIO
from blib2to3.pgen2.pgen import ParserGenerator
from tokenize import generate_tokens

@pytest.fixture(scope="module")
def parser():
    return ParserGenerator("source_code.py")



def test_parse_method():
    with pytest.raises(FileNotFoundError):
        ParserGenerator("source_code.py")

def test_addfirstsets_method():
    with pytest.raises(FileNotFoundError):
        ParserGenerator("source_code.py")