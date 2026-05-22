
import pytest
from unittest.mock import patch
from httpie.utils import parse_content_type_header

def test_parse_content_type_header_edge_case():
    with patch('httpie.utils.requests', autospec=True):
        header = None
        with pytest.raises(AttributeError):
            result = parse_content_type_header(header)
