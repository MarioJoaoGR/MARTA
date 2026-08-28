
import pytest
from io import StringIO
from unittest.mock import patch
from blib2to3.pgen2.pgen import ParserGenerator, PgenGrammar
from tokenize import generate_tokens



def test_invalid_input():
    mock_data = """
    def invalid_function {
        pass
    """
    
    with patch('blib2to3.pgen2.pgen.tokenize') as mock_tokenize:
        mock_tokenize.generate_tokens.side_effect = SyntaxError("Invalid syntax")
        with pytest.raises(SyntaxError):
            parser = ParserGenerator("dummy_filename", StringIO(mock_data))