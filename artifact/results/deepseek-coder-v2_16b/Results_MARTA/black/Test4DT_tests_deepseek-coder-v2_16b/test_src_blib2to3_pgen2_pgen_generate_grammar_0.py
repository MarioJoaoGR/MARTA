
import pytest
from blib2to3.pgen2.pgen import ParserGenerator, generate_grammar
from pathlib import Path

# Test default filename usage
def test_valid_default_filename():
    with pytest.raises(FileNotFoundError):
        grammar = generate_grammar()

# Test custom filename usage