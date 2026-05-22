
import os
from urllib.parse import urlsplit
import mimetypes
from typing import Optional
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
```

To run the test case, you would need to add a test function using `pytest` and mock any necessary dependencies. Here is an example of how you might write such a test:

```python
import pytest
from your_module import filename_from_url  # Replace 'your_module' with the actual module name where filename_from_url is defined

@pytest.mark.parametrize("url, content_type, expected", [
    ('http://example.com/path/to/resource', 'text/plain', 'index.txt'),
    ('http://example.com/path/to/resource.html', 'text/html', 'resource.html'),
    ('http://example.com/path/to/resource', None, 'index'),
])
@patch('mimetypes.guess_extension')
def test_filename_from_url(mock_guess_extension, url, content_type, expected):
    mock_guess_extension.return_value = '.txt' if content_type == 'text/plain' else None
    assert filename_from_url(url, content_type) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_downloads_filename_from_url_0_test_valid_input_with_extension
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_filename_from_url_0_test_valid_input_with_extension.py:19:1: E0001: Parsing failed: 'invalid syntax (Test4DT_tests_deepseek-coder-v2_16b.test_httpie_downloads_filename_from_url_0_test_valid_input_with_extension, line 19)' (syntax-error)


"""