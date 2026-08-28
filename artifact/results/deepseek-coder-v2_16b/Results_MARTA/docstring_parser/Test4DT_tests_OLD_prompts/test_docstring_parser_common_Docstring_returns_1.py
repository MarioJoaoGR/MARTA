
import pytest
from docstring_parser.common import Docstring, DocstringReturns

def test_none_input_returns():
    with pytest.raises(TypeError):
        doc = Docstring()
        assert doc.returns() is None
