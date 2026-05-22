
import pytest
from io import BytesIO
from unittest.mock import patch, MagicMock
import select

# Assuming the function _read_file_with_selectors is defined in a module named httpie.uploads
from httpie.uploads import _read_file_with_selectors

def test_no_data_available():
    with patch('threading.Event', autospec=True) as mock_event:
        # Create a BytesIO object without any data
        file = BytesIO(b'')

        # Create an instance of the mocked event
        read_event = MagicMock()
        mock_event.return_value = read_event

        # Call the function under test
        result = _read_file_with_selectors(file, read_event)

        # Assert that no data was read (since the file is empty)
        assert result == b''
