
import pytest
import inspect
import code
from pytutils.debug import interact

def test_default_usage():
    """Test the default usage of the interact function."""
    # Call the interact function without any arguments
    with pytest.raises(OSError):  # Expect an OSError due to captured output
        interact()

def test_custom_banner():
    """Test using a custom banner in the interact function."""
    # Call the interact function with a custom banner
    with pytest.raises(OSError):  # Expect an OSError due to captured output
        interact(banner='Welcome to the Debug Shell')

def test_usage_within_function():
    """Test calling interact from within another function."""
    def test():
        x = 10
        y = 20
        with pytest.raises(OSError):  # Expect an OSError due to captured output
            interact()
    
    # Call the nested function
    test()

def test_custom_banner_within_function():
    """Test calling interact with a custom banner from within another function."""
    def test():
        x = 10
        y = 20
        with pytest.raises(OSError):  # Expect an OSError due to captured output
            interact(banner='Testing custom banner')
    
    # Call the nested function
    test()
