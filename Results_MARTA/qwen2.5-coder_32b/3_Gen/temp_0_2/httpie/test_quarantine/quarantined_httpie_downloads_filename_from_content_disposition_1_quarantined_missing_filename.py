
import pytest
from unittest.mock import patch
from httpie.downloads import Message

def filename_from_content_disposition(content_disposition: str) -> Optional[str]:
    """
    Extract and validate filename from a Content-Disposition header.

    :param content_disposition: Content-Disposition value
    :return: the filename if present and valid, otherwise `None`
    """
    msg = Message(f'Content-Disposition: {content_disposition}')
    filename = msg.get_filename()
    if filename:
        # Basic sanitation.
        filename = os.path.basename(filename).lstrip('.').strip()
        if filename:
            return filename

@pytest.mark.parametrize("content_disposition, expected", [
    ('attachment; filename=jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz', 'jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz'),
    ('form-data; name="file"; filename=example.txt', 'example.txt'),
    ('inline; filename=no-extension', 'no-extension'),
    ('attachment', None),
])
@patch('httpie.downloads.Message')
def test_missing_filename(mock_message, content_disposition, expected):
    mock_instance = mock_message.return_value
    mock_instance.get_filename.return_value = content_disposition.split('=')[1] if '=' in content_disposition else None
    
    result = filename_from_content_disposition(content_disposition)
    assert result == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_downloads_filename_from_content_disposition_1_test_missing_filename
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_filename_from_content_disposition_1_test_missing_filename.py:6:67: E0602: Undefined variable 'Optional' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_downloads_filename_from_content_disposition_1_test_missing_filename.py:17:19: E0602: Undefined variable 'os' (undefined-variable)


"""