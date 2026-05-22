
import pytest
from unittest.mock import patch
from httpie.ssl_ import HTTPieCertificate

def test_invalid_inputs():
    cert = HTTPieCertificate()
    
    with patch('httpie.ssl_.HTTPieCertificate.cert_file', None):
        with patch('httpie.ssl_.HTTPieCertificate.key_file', None):
            assert cert.to_raw_cert() == (None, None)
    
    with patch('httpie.ssl_.HTTPieCertificate.cert_file', 'invalid_path'):
        with pytest.raises(FileNotFoundError):
            cert.to_raw_cert()

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieCertificate_to_raw_cert_0_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        cert = HTTPieCertificate()
    
        with patch('httpie.ssl_.HTTPieCertificate.cert_file', None):
            with patch('httpie.ssl_.HTTPieCertificate.key_file', None):
                assert cert.to_raw_cert() == (None, None)
    
        with patch('httpie.ssl_.HTTPieCertificate.cert_file', 'invalid_path'):
>           with pytest.raises(FileNotFoundError):
E           Failed: DID NOT RAISE <class 'FileNotFoundError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieCertificate_to_raw_cert_0_test_invalid_inputs.py:14: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl__HTTPieCertificate_to_raw_cert_0_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.22s ===============================
"""