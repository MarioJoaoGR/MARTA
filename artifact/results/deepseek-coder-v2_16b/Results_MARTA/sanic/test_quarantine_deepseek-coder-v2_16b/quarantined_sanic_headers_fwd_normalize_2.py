
import pytest
from typing import Dict, Union, List, Iterable
from urllib.parse import unquote

# Assuming fwd_normalize is defined in a module named 'sanic.headers'
def fwd_normalize(fwd: Iterable) -> Dict[str, Union[int, str]]:
    """Normalize and convert values extracted from forwarded headers."""
    ret: Dict[str, Union[int, str]] = {}
    for key, val in fwd:
        if val is not None:
            try:
                if key in ("by", "for"):
                    ret[key] = fwd_normalize_address(val)
                elif key in ("host", "proto"):
                    ret[key] = val.lower()
                elif key == "port":
                    ret[key] = int(val)
                elif key == "path":
                    ret[key] = unquote(val)
                else:
                    ret[key] = val
            except ValueError:
                pass
    return ret

def fwd_normalize_address(addr: str):
    """Helper function to normalize address strings."""
    return addr.lower()

# Test cases for valid inputs
@pytest.mark.parametrize("input_headers, expected_output", [
    ( [{'by': 'Example Corp', 'host': 'example.com', 'port': '8080', 'path': 'foo%2Bar'}], {'by': 'Example Corp', 'host': 'example.com', 'port': 8080, 'path': 'foo/bar'}),
    ( [{'proto': 'HTTP/1.1', 'for': '[2001:db8::1]'}], {'proto': 'http', 'for': '[2001:db8::1]'})
])
def test_valid_case(input_headers, expected_output):
    assert fwd_normalize(input_headers) == expected_output

# Test case for invalid protocol input
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_2.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________ test_valid_case[input_headers0-expected_output0] _______________

input_headers = [{'by': 'Example Corp', 'host': 'example.com', 'path': 'foo%2Bar', 'port': '8080'}]
expected_output = {'by': 'Example Corp', 'host': 'example.com', 'path': 'foo/bar', 'port': 8080}

    @pytest.mark.parametrize("input_headers, expected_output", [
        ( [{'by': 'Example Corp', 'host': 'example.com', 'port': '8080', 'path': 'foo%2Bar'}], {'by': 'Example Corp', 'host': 'example.com', 'port': 8080, 'path': 'foo/bar'}),
        ( [{'proto': 'HTTP/1.1', 'for': '[2001:db8::1]'}], {'proto': 'http', 'for': '[2001:db8::1]'})
    ])
    def test_valid_case(input_headers, expected_output):
>       assert fwd_normalize(input_headers) == expected_output

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_2.py:37: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

fwd = [{'by': 'Example Corp', 'host': 'example.com', 'path': 'foo%2Bar', 'port': '8080'}]

    def fwd_normalize(fwd: Iterable) -> Dict[str, Union[int, str]]:
        """Normalize and convert values extracted from forwarded headers."""
        ret: Dict[str, Union[int, str]] = {}
>       for key, val in fwd:
E       ValueError: too many values to unpack (expected 2)

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_2.py:10: ValueError
_______________ test_valid_case[input_headers1-expected_output1] _______________

input_headers = [{'for': '[2001:db8::1]', 'proto': 'HTTP/1.1'}]
expected_output = {'for': '[2001:db8::1]', 'proto': 'http'}

    @pytest.mark.parametrize("input_headers, expected_output", [
        ( [{'by': 'Example Corp', 'host': 'example.com', 'port': '8080', 'path': 'foo%2Bar'}], {'by': 'Example Corp', 'host': 'example.com', 'port': 8080, 'path': 'foo/bar'}),
        ( [{'proto': 'HTTP/1.1', 'for': '[2001:db8::1]'}], {'proto': 'http', 'for': '[2001:db8::1]'})
    ])
    def test_valid_case(input_headers, expected_output):
>       assert fwd_normalize(input_headers) == expected_output
E       AssertionError: assert {'proto': 'for'} == {'for': '[200...roto': 'http'}
E         
E         Differing items:
E         {'proto': 'for'} != {'proto': 'http'}
E         Right contains 1 more item:
E         {'for': '[2001:db8::1]'}
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_2.py:37: AssertionError
________________________ test_error_case_invalid_proto _________________________

    def test_error_case_invalid_proto():
        input_headers = [{'proto': 'InvalidProto', 'for': '[2001:db8::1]'}]
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_2.py:42: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_2.py::test_valid_case[input_headers0-expected_output0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_2.py::test_valid_case[input_headers1-expected_output1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/sanic/Test4DT_tests_deepseek-coder-v2_16b/test_sanic_headers_fwd_normalize_2.py::test_error_case_invalid_proto
============================== 3 failed in 0.06s ===============================
"""