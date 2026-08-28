
import pytest
from httpie.output.formatters.headers import HeadersFormatter

# Test initialization with enabled headers sorting
def test_headersformatter_init_with_sorting():
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    assert formatter.enabled is True

# Test initialization without headers sorting
def test_headersformatter_init_without_sorting():
    formatter = HeadersFormatter(format_options={'headers': {'sort': False}})
    assert formatter.enabled is False

# Test formatting headers with sorting enabled
def test_format_headers_with_sorting():
    raw_headers = "GET /index.html HTTP/1.1\r\nHost: example.com\r\nUser-Agent: Mozilla/5.0"
    formatter = HeadersFormatter(format_options={'headers': {'sort': True}})
    formatted_headers = formatter.format_headers(raw_headers)
    assert formatted_headers == "GET /index.html HTTP/1.1\r\nHost: example.com\r\nUser-Agent: Mozilla/5.0"

# Test formatting headers without sorting
def test_format_headers_without_sorting():
    raw_headers = "Content-Type: text/html\nDate: 2023-01-01"
    formatter = HeadersFormatter(format_options={'headers': {'sort': False}})
    formatted_headers = formatter.format_headers(raw_headers)