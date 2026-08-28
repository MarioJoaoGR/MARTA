
import pytest
from io import StringIO
from tokenize import generate_tokens, TokenInfo
from blib2to3.pgen2.tokenize import Untokenizer


def test_invalid_input():
    untokenizer = Untokenizer()
    with pytest.raises(TypeError):
        untokenizer.compat(None, None)