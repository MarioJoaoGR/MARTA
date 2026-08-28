
import pytest
from io import StringIO
from blib2to3.pgen2.pgen import ParserGenerator, NFAState
from tokenize import generate_tokens

@pytest.fixture
def parser_generator():
    content = "rule1: term1 term2 | rule2: term3 term4"
    stream = StringIO(content)
    return ParserGenerator(None, stream)


def test_edge_case_empty_input():
    stream = StringIO("")
    with pytest.raises(AssertionError):
        parser = ParserGenerator(None, stream)

def test_invalid_parse_rhs():
    content = "rule1: term1 term2 |"
    stream = StringIO(content)
    with pytest.raises(SyntaxError):
        parser = ParserGenerator(None, stream)