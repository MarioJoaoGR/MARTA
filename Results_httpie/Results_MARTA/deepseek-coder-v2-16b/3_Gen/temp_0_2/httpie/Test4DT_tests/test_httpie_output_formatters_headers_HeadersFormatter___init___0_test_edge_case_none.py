
import pytest
from unittest.mock import patch
from httpie.output.formatters.headers import HeadersFormatter

def test_edge_case_none():
    with patch('httpie.output.formatters.headers.HeadersFormatter.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            formatter = HeadersFormatter(format_options=None)
