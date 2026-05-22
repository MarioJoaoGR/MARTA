
import pytest
from unittest.mock import patch
from httpie.uploads import get_multipart_data_and_content_type

def test_get_multipart_data_and_content_type_invalid_file():
    with patch('httpie.uploads.open', side_effect=FileNotFoundError("No such file or directory: 'nonexistent_file.txt'")):
        data = {"file": ("example.txt", "nonexistent_file.txt")}
        with pytest.raises(FileNotFoundError):
            get_multipart_data_and_content_type(data)

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads_get_multipart_data_and_content_type_2_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
____________ test_get_multipart_data_and_content_type_invalid_file _____________

    def test_get_multipart_data_and_content_type_invalid_file():
        with patch('httpie.uploads.open', side_effect=FileNotFoundError("No such file or directory: 'nonexistent_file.txt'")):
            data = {"file": ("example.txt", "nonexistent_file.txt")}
>           with pytest.raises(FileNotFoundError):
E           Failed: DID NOT RAISE <class 'FileNotFoundError'>

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads_get_multipart_data_and_content_type_2_test_invalid_inputs.py:9: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads_get_multipart_data_and_content_type_2_test_invalid_inputs.py::test_get_multipart_data_and_content_type_invalid_file
============================== 1 failed in 0.23s ===============================
"""