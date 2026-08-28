
import pytest
from httpie.output.formatters.headers import HeadersFormatter



def test_headers_formatter_with_none():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    
    with pytest.raises(AttributeError):
        formatted_headers = formatter.format_headers(None)