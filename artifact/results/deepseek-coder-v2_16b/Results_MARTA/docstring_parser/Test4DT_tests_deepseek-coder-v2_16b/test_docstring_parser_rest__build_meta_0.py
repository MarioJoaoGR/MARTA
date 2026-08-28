
import pytest
import typing as T
from docstring_parser.rest import _build_meta, DocstringMeta, ParseError

# Assuming these constants are defined in the module 'docstring_parser.rest'
PARAM_KEYWORDS = ['param']
RETURNS_KEYWORDS = ['return']
YIELDS_KEYWORDS = ['yield', 'yieldeffect']  # Placeholder, adjust based on actual definition
RAISES_KEYWORDS = ['raises']

def test_edge_case_none_input():
    with pytest.raises(TypeError):
        meta = _build_meta(None, 'No description provided')
