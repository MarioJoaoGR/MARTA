
import pytest
from ansible.module_utils.urls import prepare_multipart
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Mapping, Union
import mimetypes
import base64

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_prepare_multipart_0.py F [100%]

=================================== FAILURES ===================================
___________________ test_prepare_multipart_with_valid_input ____________________

    def test_prepare_multipart_with_valid_input():
        fields = {
            'file1': {'filename': 'example.txt', 'mime_type': 'text/plain'},
            'file2': {'content': 'some content', 'filename': 'example2.txt', 'mime_type': 'application/octet-stream'},
            'text_form_field': 'value'
        }
    
        content_type, body = prepare_multipart(fields)
    
        assert isinstance(content_type, str), "Content-Type should be a string"
        assert isinstance(body, bytes), "Body should be bytes"
    
        # Parse the Content-Type header to check if it is multipart/form-data
        main_type, sub_type = content_type.split('/')
        assert main_type == 'multipart', f"Expected main type 'multipart' but got '{main_type}'"
>       assert sub_type == 'form-data', f"Expected subtype 'form-data' but got '{sub_type}'"
E       AssertionError: Expected subtype 'form-data' but got 'form-data; boundary="===============2466467293669776792=="'
E       assert 'form-data; b...3669776792=="' == 'form-data'
E         
E         - form-data
E         + form-data; boundary="===============2466467293669776792=="

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_prepare_multipart_0.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_urls_prepare_multipart_0.py::test_prepare_multipart_with_valid_input
============================== 1 failed in 0.41s ===============================
"""