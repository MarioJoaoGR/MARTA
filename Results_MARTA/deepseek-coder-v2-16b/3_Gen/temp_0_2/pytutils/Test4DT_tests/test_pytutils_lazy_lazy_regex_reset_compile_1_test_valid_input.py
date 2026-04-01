
import re
from pytutils.lazy.lazy_regex import reset_compile, _real_re_compile

def test_valid_input():
    # Save the original re.compile function
    original_compile = re.compile
    
    # Mock a new compile function for testing
    def mock_compile(*args, **kwargs):
        return "mocked_compiled"
    
    try:
        # Replace re.compile with the mocked function
        re.compile = mock_compile
        
        # Call reset_compile to restore the original function
        reset_compile()
        
        # Assert that re.compile is now the original one, not the mocked one
        assert re.compile == _real_re_compile
    finally:
        # Ensure to clean up by restoring the original re.compile if needed (though this should be automatic)
        re.compile = original_compile
