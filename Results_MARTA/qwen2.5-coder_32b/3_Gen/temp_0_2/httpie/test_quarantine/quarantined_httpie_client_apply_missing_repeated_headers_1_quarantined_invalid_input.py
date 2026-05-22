
import pytest
from httpie.client import HTTPHeadersDict, requests

def apply_missing_repeated_headers(
    original_headers: HTTPHeadersDict,
    prepared_request: requests.PreparedRequest
) -> None:
    """Update the given `prepared_request`'s headers with the original
    ones. This allows the requests to be prepared as usual, and then later
    merged with headers that are specified multiple times."""

    new_headers = HTTPHeadersDict(prepared_request.headers)
    for prepared_name, prepared_value in prepared_request.headers.items():
        if prepared_name not in original_headers:
            continue

        original_keys, original_values = zip(*filter(
            lambda item: item[0].casefold() == prepared_name.casefold(),
            original_headers.items()
        ))

        if prepared_value not in original_values:
            # If the current value is not among the initial values
            # set for this field, then it means that this field got
            # overridden on the way, and we should preserve it.
            continue

        new_headers.popone(prepared_name)
        new_headers.update(zip(original_keys, original_values))

    prepared_request.headers = new_headers

@pytest.mark.parametrize("original_headers, prepared_request", [
    (HTTPHeadersDict({'Content-Type': 'application/json'}), requests.PreparedRequest()),
    (HTTPHeadersDict({'Authorization': 'Bearer token'}), requests.PreparedRequest())
])
def test_apply_missing_repeated_headers(original_headers, prepared_request):
    apply_missing_repeated_headers(original_headers, prepared_request)
    assert len(prepared_request.headers) == len(original_headers)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_apply_missing_repeated_headers_1_test_invalid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___ test_apply_missing_repeated_headers[original_headers0-prepared_request0] ___

original_headers = <HTTPHeadersDict('Content-Type': 'application/json')>
prepared_request = <PreparedRequest [None]>

    @pytest.mark.parametrize("original_headers, prepared_request", [
        (HTTPHeadersDict({'Content-Type': 'application/json'}), requests.PreparedRequest()),
        (HTTPHeadersDict({'Authorization': 'Bearer token'}), requests.PreparedRequest())
    ])
    def test_apply_missing_repeated_headers(original_headers, prepared_request):
>       apply_missing_repeated_headers(original_headers, prepared_request)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_apply_missing_repeated_headers_1_test_invalid_input.py:39: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

original_headers = <HTTPHeadersDict('Content-Type': 'application/json')>
prepared_request = <PreparedRequest [None]>

    def apply_missing_repeated_headers(
        original_headers: HTTPHeadersDict,
        prepared_request: requests.PreparedRequest
    ) -> None:
        """Update the given `prepared_request`'s headers with the original
        ones. This allows the requests to be prepared as usual, and then later
        merged with headers that are specified multiple times."""
    
>       new_headers = HTTPHeadersDict(prepared_request.headers)
E       TypeError: 'NoneType' object is not iterable

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_apply_missing_repeated_headers_1_test_invalid_input.py:13: TypeError
___ test_apply_missing_repeated_headers[original_headers1-prepared_request1] ___

original_headers = <HTTPHeadersDict('Authorization': 'Bearer token')>
prepared_request = <PreparedRequest [None]>

    @pytest.mark.parametrize("original_headers, prepared_request", [
        (HTTPHeadersDict({'Content-Type': 'application/json'}), requests.PreparedRequest()),
        (HTTPHeadersDict({'Authorization': 'Bearer token'}), requests.PreparedRequest())
    ])
    def test_apply_missing_repeated_headers(original_headers, prepared_request):
>       apply_missing_repeated_headers(original_headers, prepared_request)

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_apply_missing_repeated_headers_1_test_invalid_input.py:39: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

original_headers = <HTTPHeadersDict('Authorization': 'Bearer token')>
prepared_request = <PreparedRequest [None]>

    def apply_missing_repeated_headers(
        original_headers: HTTPHeadersDict,
        prepared_request: requests.PreparedRequest
    ) -> None:
        """Update the given `prepared_request`'s headers with the original
        ones. This allows the requests to be prepared as usual, and then later
        merged with headers that are specified multiple times."""
    
>       new_headers = HTTPHeadersDict(prepared_request.headers)
E       TypeError: 'NoneType' object is not iterable

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_apply_missing_repeated_headers_1_test_invalid_input.py:13: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_apply_missing_repeated_headers_1_test_invalid_input.py::test_apply_missing_repeated_headers[original_headers0-prepared_request0]
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_client_apply_missing_repeated_headers_1_test_invalid_input.py::test_apply_missing_repeated_headers[original_headers1-prepared_request1]
============================== 2 failed in 0.22s ===============================
"""