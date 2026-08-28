
import pytest
from unittest.mock import patch
import os

def atexit_remove_file(filename):
    if os.path.exists(filename):
        try:
            os.unlink(filename)
        except Exception:
            # just ignore if we cannot delete, things should be ok
            pass

@pytest.fixture(autouse=True)
def cleanup_file():
    test_file = '/tmp/test_file'
    with patch('os.path.exists', return_value=False):  # Ensure file does not exist initially
        yield
    assert not os.path.exists(test_file), "File should be deleted upon script exit"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_atexit_remove_file_0.py F [100%]

=================================== FAILURES ===================================
________________________ test_atexit_remove_file_basic _________________________

    def test_atexit_remove_file_basic():
        with patch('os.path.exists', return_value=True):  # Mock the file to exist initially
            atexit_remove_file('/tmp/test_file')
>           assert not os.path.exists('/tmp/test_file'), "File should be deleted upon script exit"
E           AssertionError: File should be deleted upon script exit
E           assert not True
E            +  where True = <MagicMock name='exists' id='139889976252624'>('/tmp/test_file')
E            +    where <MagicMock name='exists' id='139889976252624'> = <module 'posixpath' from '/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py'>.exists
E            +      where <module 'posixpath' from '/opt/conda/envs/test4py_env/lib/python3.10/posixpath.py'> = os.path

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_atexit_remove_file_0.py:24: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_atexit_remove_file_0.py::test_atexit_remove_file_basic
============================== 1 failed in 0.22s ===============================
"""