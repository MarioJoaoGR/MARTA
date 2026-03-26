
import pytest
from docstring_parser.rest import _build_meta, DocstringMeta

def test_edge_cases():
    # Test None input
    with pytest.raises(IndexError):
        assert _build_meta([], "No args") is not None
