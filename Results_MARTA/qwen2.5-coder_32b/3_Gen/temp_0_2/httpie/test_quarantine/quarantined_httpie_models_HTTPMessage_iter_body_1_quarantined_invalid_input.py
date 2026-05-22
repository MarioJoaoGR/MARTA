
import pytest
from httpie.models import HTTPMessage

class TestHTTPMessage:
    def test_iter_body(self):
        msg = HTTPMessage(orig={'body': b'a'*1024})
        
        with pytest.raises(ValueError):
            list(msg.iter_body(-1))

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_iter_body_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
________________________ TestHTTPMessage.test_iter_body ________________________

self = <test_httpie_models_HTTPMessage_iter_body_1_test_invalid_input.TestHTTPMessage object at 0x7f2f525093d0>

    def test_iter_body(self):
        msg = HTTPMessage(orig={'body': b'a'*1024})
    
        with pytest.raises(ValueError):
>           list(msg.iter_body(-1))

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_iter_body_1_test_invalid_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <httpie.models.HTTPMessage object at 0x7f2f51d6a3d0>, chunk_size = -1

    def iter_body(self, chunk_size: int) -> Iterable[bytes]:
        """Return an iterator over the body."""
>       raise NotImplementedError
E       NotImplementedError

httpie/httpie/models.py:31: NotImplementedError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_models_HTTPMessage_iter_body_1_test_invalid_input.py::TestHTTPMessage::test_iter_body
============================== 1 failed in 0.13s ===============================
"""