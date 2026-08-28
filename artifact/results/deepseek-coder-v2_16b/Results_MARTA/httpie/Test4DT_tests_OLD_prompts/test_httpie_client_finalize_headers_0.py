
import pytest
from httpie.client import RequestHeadersDict

def finalize_headers(headers: RequestHeadersDict) -> RequestHeadersDict:
    final_headers = RequestHeadersDict()
    for name, value in headers.items():
        if value is not None:
            # “leading or trailing LWS MAY be removed without
            # changing the semantics of the field value”
            # <https://www.w3.org/Protocols/rfc2616/rfc2616-sec4.html>
            # Also, requests raises `InvalidHeader` for leading spaces.
            value = value.strip()
            if isinstance(value, str):
                # See <https://github.com/httpie/httpie/issues/212>
                value = value.encode('utf8')
        final_headers[name] = value
    return final_headers


def test_empty_headers():
    headers = RequestHeadersDict({})
    finalized_headers = finalize_headers(headers)
    assert len(finalized_headers) == 0, "Expected empty headers to remain empty"

def test_headers_with_whitespace():
    headers = RequestHeadersDict({'Content-Type': ' application/json ', 'User-Agent': ' httpie '})
    finalized_headers = finalize_headers(headers)
    assert finalized_headers['Content-Type'] == b'application/json', "Expected whitespace to be stripped from header values"
    assert finalized_headers['User-Agent'] == b'httpie', "Expected whitespace to be stripped from header values"
