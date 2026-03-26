
import pytest
from unittest.mock import patch, MagicMock
from flutes.network import _download_from_google_drive

@pytest.mark.parametrize("url, filename, path", [
    ("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view?usp=sharing", "myfile.txt", "./downloads")
])
def test_valid_input(url, filename, path):
    with patch('requests.Session') as mock_session:
        mock_response = MagicMock()
        mock_response.iter_content.return_value = [b'chunk1', b'chunk2']
        mock_session().get.return_value = mock_response
        
        with patch('os.path.join', return_value='./downloads/myfile.txt'):
            result = _download_from_google_drive(url, filename, path)
            assert result == './downloads/myfile.txt'
