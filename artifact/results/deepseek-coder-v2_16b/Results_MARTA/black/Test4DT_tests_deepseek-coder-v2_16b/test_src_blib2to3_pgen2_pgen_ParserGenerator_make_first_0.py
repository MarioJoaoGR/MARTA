
import pytest
from pathlib import Path
from io import StringIO
from blib2to3.pgen2.pgen import ParserGenerator, PgenGrammar
from tokenize import generate_tokens

@pytest.fixture
def parser():
    return ParserGenerator("dummy_file")


@pytest.mark.parametrize("filename", ["dummy_file"])
def test_invalid_input(filename):
    with pytest.raises(FileNotFoundError):
        ParserGenerator(filename)

def test_edge_case():
    with pytest.raises(FileNotFoundError):
        ParserGenerator("dummy_file")