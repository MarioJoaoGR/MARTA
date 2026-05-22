
import pytest
from unittest.mock import patch, MagicMock
from httpie.downloads import filename_from_content_disposition

def test_invalid_input():
    with patch('httpie.downloads.Message', autospec=True) as mock_message:
        mock_message.return_value = MagicMock()
        mock_message.return_value.get_filename.return_value = None
        
        assert filename_from_content_disposition('invalid-header') is None
