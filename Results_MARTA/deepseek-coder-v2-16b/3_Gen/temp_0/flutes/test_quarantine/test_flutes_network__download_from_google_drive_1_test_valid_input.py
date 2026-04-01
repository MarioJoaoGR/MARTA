
import os
from unittest.mock import patch
import pytest
from flutes.network import _download_from_google_drive, _extract_google_drive_file_id

@pytest.mark.parametrize("url, filename, path", [
    ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing", "myfile.txt", "/home/user"),
    ("https://drive.google.com/uc?export=download&id=1aBcD2eF3gHiJkLmNoPqRsT", "myfile.txt", "/home/user")
])
@patch('flutes.network._extract_google_drive_file_id')
def test_valid_input(mock_extract, url, filename, path):
    mock_extract.return_value = "1aBcD2eF3gHiJkLmNoPqRsT"  # Mock the file ID extraction

    expected_filepath = f"/home/user/{filename}"
    actual_filepath = _download_from_google_drive(url, filename, path)

    assert os.path.exists(actual_filepath), f"File {actual_filepath} does not exist."
    assert actual_filepath == expected_filepath, f"Expected filepath {expected_filepath}, but got {actual_filepath}"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_ test_valid_input[https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing-myfile.txt-/home/user] _

mock_extract = <MagicMock name='_extract_google_drive_file_id' id='140192224446800'>
url = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing'
filename = 'myfile.txt', path = '/home/user'

    @pytest.mark.parametrize("url, filename, path", [
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing", "myfile.txt", "/home/user"),
        ("https://drive.google.com/uc?export=download&id=1aBcD2eF3gHiJkLmNoPqRsT", "myfile.txt", "/home/user")
    ])
    @patch('flutes.network._extract_google_drive_file_id')
    def test_valid_input(mock_extract, url, filename, path):
        mock_extract.return_value = "1aBcD2eF3gHiJkLmNoPqRsT"  # Mock the file ID extraction
    
        expected_filepath = f"/home/user/{filename}"
>       actual_filepath = _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_valid_input.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

url = 'https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing'
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
_ test_valid_input[https://drive.google.com/uc?export=download&id=1aBcD2eF3gHiJkLmNoPqRsT-myfile.txt-/home/user] _

mock_extract = <MagicMock name='_extract_google_drive_file_id' id='140192216967632'>
url = 'https://drive.google.com/uc?export=download&id=1aBcD2eF3gHiJkLmNoPqRsT'
filename = 'myfile.txt', path = '/home/user'

    @pytest.mark.parametrize("url, filename, path", [
        ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing", "myfile.txt", "/home/user"),
        ("https://drive.google.com/uc?export=download&id=1aBcD2eF3gHiJkLmNoPqRsT", "myfile.txt", "/home/user")
    ])
    @patch('flutes.network._extract_google_drive_file_id')
    def test_valid_input(mock_extract, url, filename, path):
        mock_extract.return_value = "1aBcD2eF3gHiJkLmNoPqRsT"  # Mock the file ID extraction
    
        expected_filepath = f"/home/user/{filename}"
>       actual_filepath = _download_from_google_drive(url, filename, path)

flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_valid_input.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

url = 'https://drive.google.com/uc?export=download&id=1aBcD2eF3gHiJkLmNoPqRsT'
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
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_valid_input.py::test_valid_input[https:/drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing-myfile.txt-/home/user]
FAILED flutes/Test4DT_tests/test_flutes_network__download_from_google_drive_1_test_valid_input.py::test_valid_input[https:/drive.google.com/uc?export=download&id=1aBcD2eF3gHiJkLmNoPqRsT-myfile.txt-/home/user]
============================== 2 failed in 1.74s ===============================
"""