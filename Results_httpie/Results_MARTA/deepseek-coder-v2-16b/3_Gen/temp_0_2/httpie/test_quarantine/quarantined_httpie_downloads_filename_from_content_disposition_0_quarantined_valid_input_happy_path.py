
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

@pytest.mark.parametrize("input, expected", [
    ('attachment; filename=jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz', 'jakubroztocil-httpie-0.4.1-20-g40bd8f6.tar.gz'),
    ('form-data; name="file"; filename=example.txt', 'example.txt'),
    ('inline; filename=no-extension', 'no-extension'),
    ('attachment', None),
])
def test_valid_input_happy_path(input, expected):
    with patch('httpie.downloads.Message') as mock_message:
        instance = mock_message.return_value
        instance.get_filename.return_value = input.split('=')[1] if '=' in input else None
        assert filename_from_content_disposition(input) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_downloads_filename_from_content_disposition_0_test_valid_input_happy_path
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_filename_from_content_disposition_0_test_valid_input_happy_path.py:6:67: E0602: Undefined variable 'Optional' (undefined-variable)
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_downloads_filename_from_content_disposition_0_test_valid_input_happy_path.py:17:19: E0602: Undefined variable 'os' (undefined-variable)


"""