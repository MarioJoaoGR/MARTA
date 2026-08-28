
import pytest
import re

def _cleanup_filename(s):
    if s is None:
        return '_'
    return '_'.join(re.sub('[^a-zA-Z0-9]', ' ', s).split())

# Test cases for _cleanup_filename function

@pytest.mark.parametrize("input_string, expected", [
    ('example!@#file.txt', 'example_file_txt'),
    (None, '_'),
    ('important file 123-456.docx', 'important_file_123_456_docx')
])
def test_cleanup_filename(input_string, expected):
    assert _cleanup_filename(input_string) == expected
