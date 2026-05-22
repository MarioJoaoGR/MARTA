
from httpie.models import parse_content_type_header, HTTPMessage
from unittest.mock import patch

def test_HTTPMessage_encoding_basic():
    with patch('httpie.models.parse_content_type_header', return_value=('', {'charset': 'utf-8'})):
        msg = HTTPMessage('text/html; charset=utf-8')
        assert msg.encoding() == 'utf-8'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_encoding_0_test_HTTPMessage_encoding_basic.py F [100%]

=================================== FAILURES ===================================
_______________________ test_HTTPMessage_encoding_basic ________________________

    def test_HTTPMessage_encoding_basic():
        with patch('httpie.models.parse_content_type_header', return_value=('', {'charset': 'utf-8'})):
            msg = HTTPMessage('text/html; charset=utf-8')
>           assert msg.encoding() == 'utf-8'

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_encoding_0_test_HTTPMessage_encoding_basic.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/functools.py:1001: in __get__
    val = self.func(instance)
httpie/httpie/models.py:49: in encoding
    ct, params = parse_content_type_header(self.content_type)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.models.HTTPMessage object at 0x7f3ac09e7c50>

    @property
    def content_type(self) -> str:
        """Return the message content type."""
>       ct = self._orig.headers.get('Content-Type', '')
E       AttributeError: 'str' object has no attribute 'headers'

httpie/httpie/models.py:55: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_encoding_0_test_HTTPMessage_encoding_basic.py::test_HTTPMessage_encoding_basic
============================== 1 failed in 0.11s ===============================
"""