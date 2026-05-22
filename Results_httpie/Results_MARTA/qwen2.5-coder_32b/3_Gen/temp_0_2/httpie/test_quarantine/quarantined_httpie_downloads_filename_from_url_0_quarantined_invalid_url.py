
import os
from urllib.parse import urlsplit
import mimetypes
from unittest.mock import patch

def filename_from_url(url: str, content_type: Optional[str]) -> str:
    fn = urlsplit(url).path.rstrip('/')
    fn = os.path.basename(fn) if fn else 'index'
    if '.' not in fn and content_type:
        content_type = content_type.split(';')[0]
        ext = mimetypes.guess_extension(content_type)
        if ext == '.htm':
            ext = '.html'
        if ext:
            fn += ext
    return fn

# Test case for invalid URL
def test_invalid_url():
    with patch('mimetypes.guess_extension') as mock_guess_extension:
        # Mock the guess_extension to always return .txt
        mock_guess_extension.return_value = '.txt'
        
        url = 'http://example.com/path/to/resource'
        content_type = 'text/plain'
        
        expected_filename = 'index.txt'
        assert filename_from_url(url, content_type) == expected_filename

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_downloads_filename_from_url_0_test_invalid_url
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_filename_from_url_0_test_invalid_url.py:7:46: E0602: Undefined variable 'Optional' (undefined-variable)


"""