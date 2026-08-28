
import pytest
from pathlib import Path
from io import StringIO
from blib2to3.pgen2.pgen import ParserGenerator
from tokenize import generate_tokens, COMMENT, NL


def test_edge_case():
    with pytest.raises(TypeError):
        ParserGenerator()
