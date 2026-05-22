
import pytest
from httpie.ssl_ import _is_key_file_encrypted

@pytest.fixture
def create_temp_key_file():
    # Create a temporary key file for testing
    with open('/tmp/test_key_file.txt', 'w') as f:
        f.write("Some content without ENCRYPTED")
    yield '/tmp/test_key_file.txt'
    # Clean up the temporary file after the test
    import os
    os.remove('/tmp/test_key_file.txt')

def test_missing_encrypted_line(create_temp_key_file):
    assert not _is_key_file_encrypted(create_temp_key_file), "Expected the key file to be unencrypted"

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

httpie/Test4DT_tests_codestral/test_httpie_ssl___is_key_file_encrypted_2_test_missing_encrypted_line.py F [100%]

=================================== FAILURES ===================================
_________________________ test_missing_encrypted_line __________________________

create_temp_key_file = '/tmp/test_key_file.txt'

    def test_missing_encrypted_line(create_temp_key_file):
>       assert not _is_key_file_encrypted(create_temp_key_file), "Expected the key file to be unencrypted"
E       AssertionError: Expected the key file to be unencrypted
E       assert not True
E        +  where True = _is_key_file_encrypted('/tmp/test_key_file.txt')

httpie/Test4DT_tests_codestral/test_httpie_ssl___is_key_file_encrypted_2_test_missing_encrypted_line.py:16: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_ssl___is_key_file_encrypted_2_test_missing_encrypted_line.py::test_missing_encrypted_line
============================== 1 failed in 0.16s ===============================
"""