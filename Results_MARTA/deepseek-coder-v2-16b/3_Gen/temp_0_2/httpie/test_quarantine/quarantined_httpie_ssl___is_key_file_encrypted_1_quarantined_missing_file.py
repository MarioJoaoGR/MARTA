
import pytest
from unittest.mock import patch, MagicMock
from httpie.ssl_ import _is_key_file_encrypted

def test_missing_file():
    with patch('os.path.exists', MagicMock(return_value=False)):
        key_file = 'non_existent_file'
        assert not _is_key_file_encrypted(key_file)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl___is_key_file_encrypted_1_test_missing_file.py F [100%]

=================================== FAILURES ===================================
______________________________ test_missing_file _______________________________

    def test_missing_file():
        with patch('os.path.exists', MagicMock(return_value=False)):
            key_file = 'non_existent_file'
>           assert not _is_key_file_encrypted(key_file)

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl___is_key_file_encrypted_1_test_missing_file.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

key_file = 'non_existent_file'

    def _is_key_file_encrypted(key_file):
        """Detects if a key file is encrypted or not.
    
        Copy of the internal urllib function (urllib3.util.ssl_)"""
    
>       with open(key_file, "r") as f:
E       FileNotFoundError: [Errno 2] No such file or directory: 'non_existent_file'

httpie/httpie/ssl_.py:97: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_ssl___is_key_file_encrypted_1_test_missing_file.py::test_missing_file
============================== 1 failed in 0.13s ===============================
"""