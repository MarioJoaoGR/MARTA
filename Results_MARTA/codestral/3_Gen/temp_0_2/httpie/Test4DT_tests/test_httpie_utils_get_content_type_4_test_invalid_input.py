
import pytest
from unittest.mock import patch
import mimetypes

def get_content_type(filename):
    """
    Return the content type for ``filename`` in format appropriate
    for Content-Type headers, or ``None`` if the file type is unknown
    to ``mimetypes``.

    """
    return mimetypes.guess_type(filename, strict=False)[0]

@pytest.fixture(params=[
    "example.txt",
    "report.pdf",
    "unknownfile.xyz"
])
def test_data(request):
    return request.param

def test_get_content_type_invalid_input(test_data):
    with patch('mimetypes.guess_type') as mock_guess_type:
        # Mock the behavior of guess_type based on the input filename
        if "example.txt" in test_data:
            mock_guess_type.return_value = ('text/plain', None)
        elif "report.pdf" in test_data:
            mock_guess_type.return_value = ('application/pdf', None)
        else:
            mock_guess_type.return_value = (None, None)
        
        # Call the function with the test data
        result = get_content_type(test_data)
        
        # Check if the result matches the expected outcome based on the mocked behavior
        assert result == ('text/plain' if "example.txt" in test_data else 'application/pdf' if "report.pdf" in test_data else None)
