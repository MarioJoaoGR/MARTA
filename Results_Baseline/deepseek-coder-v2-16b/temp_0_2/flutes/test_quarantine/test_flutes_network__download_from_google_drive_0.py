
import pytest
from unittest.mock import patch, MagicMock
import requests
import os
from flutes.network import _download_from_google_drive

# Mock data for testing
TEST_URL = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZa/view?usp=sharing'
TEST_FILENAME = 'myfile.txt'
TEST_PATH = '/home/user'

def test_download_from_google_drive():
    with patch('requests.Session.get') as mock_get:
        # Mock the response from requests.Session.get
        mock_response = MagicMock()
        mock_response.iter_content.return_value = [b'chunk1', b'chunk2']  # Example chunks
        mock_response.cookies = {'download_warning': 'token'}
        mock_get.return_value = mock_response
        
        expected_filepath = os.path.join(TEST_PATH, TEST_FILENAME)
        actual_filepath = _download_from_google_drive(TEST_URL, TEST_FILENAME, TEST_PATH)
        
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0.py F [100%]

=================================== FAILURES ===================================
_______________________ test_download_from_google_drive ________________________

    def test_download_from_google_drive():
        with patch('requests.Session.get') as mock_get:
            # Mock the response from requests.Session.get
            mock_response = MagicMock()
            mock_response.iter_content.return_value = [b'chunk1', b'chunk2']  # Example chunks
            mock_response.cookies = {'download_warning': 'token'}
            mock_get.return_value = mock_response
    
            expected_filepath = os.path.join(TEST_PATH, TEST_FILENAME)
>           actual_filepath = _download_from_google_drive(TEST_URL, TEST_FILENAME, TEST_PATH)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

url = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZa/view?usp=sharing'
filename = 'myfile.txt', path = '/home/user', bar_fn = None

    def _download_from_google_drive(url: str, filename: str, path: str, bar_fn: Optional[BarFn] = None) -> str:
        # Credit: https://github.com/saurabhshri/gdrive-downloader
        import requests
    
        def _get_confirm_token(resp):
            for key, value in resp.cookies.items():
                if key.startswith('download_warning'):
                    return value
            return None
    
        file_id = _extract_google_drive_file_id(url)
    
        gurl = "https://docs.google.com/uc?export=download"
        sess = requests.Session()
        response = sess.get(gurl, params={'id': file_id}, stream=True)
        token = _get_confirm_token(response)
    
        if token:
            params = {'id': file_id, 'confirm': token}
            response = sess.get(gurl, params=params, stream=True)
    
        filepath = os.path.join(path, filename)
        CHUNK_SIZE = 32768
        progress = bar_fn() if bar_fn is not None else None
>       with open(filepath, "wb") as f:
E       FileNotFoundError: [Errno 2] No such file or directory: '/home/user/myfile.txt'

flutes/flutes/network.py:142: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_0.py::test_download_from_google_drive
============================== 1 failed in 0.14s ===============================
"""