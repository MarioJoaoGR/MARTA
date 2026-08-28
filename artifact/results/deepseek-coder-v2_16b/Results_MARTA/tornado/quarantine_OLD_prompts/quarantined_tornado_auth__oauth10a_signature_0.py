
import pytest
from unittest.mock import patch, MagicMock
import urllib.parse
import hmac
import hashlib
import binascii
from typing import Dict, Any, Optional

def _oauth10a_signature(
    consumer_token: Dict[str, Any],
    method: str,
    url: str,
    parameters: Dict[str, Any] = {},
    token: Optional[Dict[str, Any]] = None,
) -> bytes:
    """Calculates the HMAC-SHA1 OAuth 1.0a signature for the given request."""
    parts = urllib.parse.urlparse(url)
    scheme, netloc, path = parts[:3]
    normalized_url = scheme.lower() + "://" + netloc.lower() + path

    base_elems = []
    base_elems.append(method.upper())
    base_elems.append(normalized_url)
    base_elems.append(
        "&".join(
            "%s=%s" % (k, _oauth_escape(str(v))) for k, v in sorted(parameters.items())
        )
    )

    base_string = "&".join(_oauth_escape(e) for e in base_elems)
    key_elems = [urllib.parse.quote(consumer_token["secret"], safe="~")]
    if token:
        key_elems.append(urllib.parse.quote(token["secret"], safe="~"))
    key = "&".join(key_elems)

    hash = hmac.new(key.encode(), base_string.encode(), hashlib.sha1)
    return binascii.b2a_base64(hash.digest())[:-1]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth10a_signature_0.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with pytest.raises(TypeError) as excinfo:
            consumer_token = None
            method = 'GET'
            url = 'https://api.example.com/resource?param=value'
>           _oauth10a_signature(consumer_token, method, url)

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth10a_signature_0.py:45: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth10a_signature_0.py:31: in _oauth10a_signature
    base_string = "&".join(_oauth_escape(e) for e in base_elems)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <list_iterator object at 0x7f237ec3c1f0>

>   base_string = "&".join(_oauth_escape(e) for e in base_elems)
E   NameError: name '_oauth_escape' is not defined

/opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth10a_signature_0.py:31: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/tornado/Test4DT_tests_deepseek-coder-v2_16b/test_tornado_auth__oauth10a_signature_0.py::test_invalid_inputs
============================== 1 failed in 0.10s ===============================
"""