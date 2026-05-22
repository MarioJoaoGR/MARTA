
import pytest
from unittest.mock import patch, MagicMock
from requests_toolbelt import MultipartEncoder
from typing import Tuple

def get_multipart_data_and_content_type(
    data: dict,
    boundary: str = None,
    content_type: str = None,
) -> Tuple[MultipartEncoder, str]:
    from requests_toolbelt import MultipartEncoder

    encoder = MultipartEncoder(
        fields=data.items(),
        boundary=boundary,
    )
    if content_type:
        content_type = content_type.strip()
        if 'boundary=' not in content_type:
            content_type = f'{content_type}; boundary={encoder.boundary_value}'
    else:
        content_type = encoder.content_type

    return encoder, content_type

@pytest.fixture(scope="module")
def valid_input():
    data = {'file': ('example.txt', open('example.txt', 'rb')), 'description': 'This is a test upload.'}
    return data

@pytest.mark.parametrize("data", [valid_input()])
def test_valid_input(data, monkeypatch):
    with patch('requests_toolbelt.MultipartEncoder', autospec=True) as MockMultipartEncoder:
        mock_encoder = MagicMock()
        mock_encoder.boundary_value = "testboundary"
        mock_encoder.content_type = f'multipart/form-data; boundary={mock_encoder.boundary_value}'
        
        monkeypatch.setattr(get_multipart_data_and_content_type, 'MultipartEncoder', lambda *args, **kwargs: mock_encoder)
        
        multipart_data, content_type = get_multipart_data_and_content_type(data)
        
        assert isinstance(multipart_data, MultipartEncoder)
        assert content_type == f'multipart/form-data; boundary={mock_encoder.boundary_value}'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items / 1 error

==================================== ERRORS ====================================
_ ERROR collecting Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads_get_multipart_data_and_content_type_0_test_valid_input.py _
Fixture "valid_input" called directly. Fixtures are not meant to be called directly,
but are created automatically when test functions request them as parameters.
See https://docs.pytest.org/en/stable/explanation/fixtures.html for more information about fixtures, and
https://docs.pytest.org/en/stable/deprecations.html#calling-fixtures-directly about how to update your code.
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_uploads_get_multipart_data_and_content_type_0_test_valid_input.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.17s ===============================
"""