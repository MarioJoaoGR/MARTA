
import re
from unittest.mock import patch, MagicMock
import pytutils.lazy.lazy_regex

def test_reset_compile():
    # Save the original compile function for comparison later
    original_compile = re.compile
    
    # Mocking to simulate a change in re.compile
    mock_compile = MagicMock()
    with patch('re.compile', mock_compile):
        from pytutils.lazy.lazy_regex import reset_compile
        
        # Call the function under test
        reset_compile()
        
        # Check if re.compile has been restored to its original state
        assert re.compile == original_compile
