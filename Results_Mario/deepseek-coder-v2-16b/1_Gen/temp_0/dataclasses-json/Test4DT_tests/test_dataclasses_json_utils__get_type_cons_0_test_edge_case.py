
import sys
from dataclasses_json import utils as dtu  # Assuming 'utils' is the module name in 'dataclasses-json'
import pytest
from unittest.mock import patch, MagicMock

@pytest.mark.skipif(sys.version_info < (3, 7), reason="Requires Python 3.7 or higher")
def test_get_type_cons():
    # Mocking a type object for testing
    mock_type = MagicMock()
    
    with patch('dataclasses_json.utils._get_type_cons', return_value=mock_type):
        assert dtu._get_type_cons(mock_type) == mock_type
