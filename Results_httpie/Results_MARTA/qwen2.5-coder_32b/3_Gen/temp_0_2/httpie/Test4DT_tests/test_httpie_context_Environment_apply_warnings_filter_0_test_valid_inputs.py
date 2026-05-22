
import pytest
from unittest.mock import patch
from httpie.context import Environment

@pytest.fixture(scope="function")
def environment():
    return Environment()

def test_apply_warnings_filter(environment):
    with patch('httpie.context.warnings') as mock_warnings:
        # Set the quiet level to a value that should trigger the warning filter
        environment.quiet = 1
        
        # Call the method under test
        environment.apply_warnings_filter()
        
        # Assert that the warnings filter was applied correctly
        assert mock_warnings.simplefilter.called_with("ignore")
