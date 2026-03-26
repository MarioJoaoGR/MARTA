
import pytest
from pytutils.urls import update_query_params

def test_invalid_input():
    with pytest.raises(TypeError):
        update_query_params(12345, {'foo': 'bar'})  # Invalid URL type

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_2_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(TypeError):
>           update_query_params(12345, {'foo': 'bar'})  # Invalid URL type

pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_2_test_invalid_input.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
pytutils/pytutils/urls.py:23: in update_query_params
    scheme, netloc, path, query_string, fragment = urlparse.urlsplit(url)
/usr/local/lib/python3.11/urllib/parse.py:491: in urlsplit
    url, scheme, _coerce_result = _coerce_args(url, scheme)
/usr/local/lib/python3.11/urllib/parse.py:133: in _coerce_args
    return _decode_args(args) + (_encode_result,)
/usr/local/lib/python3.11/urllib/parse.py:117: in _decode_args
    return tuple(x.decode(encoding, errors) if x else '' for x in args)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <tuple_iterator object at 0x7f659787dd50>

>   return tuple(x.decode(encoding, errors) if x else '' for x in args)
E   AttributeError: 'int' object has no attribute 'decode'

/usr/local/lib/python3.11/urllib/parse.py:117: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED pytutils/Test4DT_tests/test_pytutils_urls_update_query_params_2_test_invalid_input.py::test_invalid_input
============================== 1 failed in 0.08s ===============================
"""