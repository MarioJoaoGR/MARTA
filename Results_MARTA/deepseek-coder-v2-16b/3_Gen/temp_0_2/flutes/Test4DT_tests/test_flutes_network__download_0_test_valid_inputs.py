
import os
import urllib.request
from unittest.mock import MagicMock, patch
import pytest
from flutes.network import _download, BarFn

@pytest.mark.parametrize("url, filename, path", [
    ("http://example.com/file.zip", "file.zip", "/path/to/save"),
    ("https://example.com/file.zip", "file.zip", "/path/to/save")
])
def test_valid_inputs(url, filename, path):
    # Mock the bar_fn if provided
    bar_fn = MagicMock()
    
    with patch('urllib.request.urlretrieve') as mock_urlretrieve:
        mock_urlretrieve.side_effect = urllib.error.HTTPError(None, 404, 'Not Found', {}, None)
        
        # Call the function with valid inputs
        with pytest.raises(urllib.error.HTTPError):
            result = _download(url, filename, path, bar_fn)
