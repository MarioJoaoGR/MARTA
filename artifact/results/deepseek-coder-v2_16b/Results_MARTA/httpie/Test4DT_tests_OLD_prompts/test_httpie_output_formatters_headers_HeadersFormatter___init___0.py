
import pytest
from httpie.output.formatters.headers import HeadersFormatter

def test_edge_case_none():
    with pytest.raises(TypeError):
        formatter = HeadersFormatter(format_options=None)
