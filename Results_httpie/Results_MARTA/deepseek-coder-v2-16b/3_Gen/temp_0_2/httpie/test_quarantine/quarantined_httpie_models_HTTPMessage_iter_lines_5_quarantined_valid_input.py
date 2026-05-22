
import unittest
from httpie.models import HTTPMessage
from typing import Iterable

class TestHTTPMessageIterLines(unittest.TestCase):
    def test_valid_input(self):
        class MyHTTPMessage(HTTPMessage):
            def iter_lines(self, chunk_size: int) -> Iterable[bytes]:
                body = self._orig['body']  # Assuming the original data contains a 'body' key
                for line in body.split(b'\n'):
                    yield line + b'\r\n'
        
        msg = MyHTTPMessage({'body': b'Line1\nLine2\nLine3'})
        result = [line.decode() for line, _ in msg.iter_lines(chunk_size=10)]
        self.assertEqual(result, ['Line1', 'Line2', 'Line3'])

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_iter_lines_5_test_valid_input.py F [100%]

=================================== FAILURES ===================================
__________________ TestHTTPMessageIterLines.test_valid_input ___________________

self = <test_httpie_models_HTTPMessage_iter_lines_5_test_valid_input.TestHTTPMessageIterLines testMethod=test_valid_input>

    def test_valid_input(self):
        class MyHTTPMessage(HTTPMessage):
            def iter_lines(self, chunk_size: int) -> Iterable[bytes]:
                body = self._orig['body']  # Assuming the original data contains a 'body' key
                for line in body.split(b'\n'):
                    yield line + b'\r\n'
    
        msg = MyHTTPMessage({'body': b'Line1\nLine2\nLine3'})
>       result = [line.decode() for line, _ in msg.iter_lines(chunk_size=10)]

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_iter_lines_5_test_valid_input.py:15: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

.0 = <generator object TestHTTPMessageIterLines.test_valid_input.<locals>.MyHTTPMessage.iter_lines at 0x7f2fe4a29540>

>   result = [line.decode() for line, _ in msg.iter_lines(chunk_size=10)]
E   ValueError: too many values to unpack (expected 2)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_iter_lines_5_test_valid_input.py:15: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_models_HTTPMessage_iter_lines_5_test_valid_input.py::TestHTTPMessageIterLines::test_valid_input
============================== 1 failed in 0.20s ===============================
"""