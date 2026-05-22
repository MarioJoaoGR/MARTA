
import pytest
from unittest.mock import patch
from httpie.uploads import get_multipart_data_and_content_type

def test_invalid_inputs():
    with patch('httpie.uploads.open', side_effect=FileNotFoundError("No such file or directory: 'nonexistent_file.txt'")):
        data = {"file": ("example.txt", open("nonexistent_file.txt", 'rb'))}
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

httpie/Test4DT_tests_codestral/test_httpie_uploads_get_multipart_data_and_content_type_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('httpie.uploads.open', side_effect=FileNotFoundError("No such file or directory: 'nonexistent_file.txt'")):
>           data = {"file": ("example.txt", open("nonexistent_file.txt", 'rb'))}
E           FileNotFoundError: [Errno 2] No such file or directory: 'nonexistent_file.txt'

httpie/Test4DT_tests_codestral/test_httpie_uploads_get_multipart_data_and_content_type_1_test_invalid_inputs.py:8: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_uploads_get_multipart_data_and_content_type_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.21s ===============================
"""