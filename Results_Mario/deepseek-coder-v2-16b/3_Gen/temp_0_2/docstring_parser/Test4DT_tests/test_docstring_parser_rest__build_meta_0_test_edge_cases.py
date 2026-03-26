
import pytest
from docstring_parser.rest import _build_meta, DocstringMeta

def test_edge_cases():
    # Test with None values
    with pytest.raises(TypeError):
        assert isinstance(_build_meta(args=None, desc=""), DocstringMeta)
