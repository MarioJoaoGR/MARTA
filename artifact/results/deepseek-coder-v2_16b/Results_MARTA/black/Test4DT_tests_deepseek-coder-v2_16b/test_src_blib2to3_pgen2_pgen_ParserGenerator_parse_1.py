
import pytest
from pathlib import Path
from io import StringIO
from tokenize import generate_tokens
from blib2to3.pgen2.pgen import ParserGenerator

@pytest.fixture
def parser_generator():
    # Create a temporary file with the provided source code for testing
    source_code = """
NAME : 'print(\'Hello, World!\')' NEWLINE
"""
    stream = StringIO(source_code)
    return ParserGenerator(None, stream)


def test_invalid_input():
    # Create a temporary file with invalid source code for testing
    source_code = """
INVALID : 'print('Hello, World!')' NEWLINE
"""
    stream = StringIO(source_code)
    
    with pytest.raises(SyntaxError):
        parser = ParserGenerator(None, stream)