
import pytest
import re
from pytutils.lazy.lazy_regex import install_lazy_compile, reset_compile


def test_reset_compile():
    # Backup the current re.compile method
    original_compile = re.compile
    
    try:
        # Install lazy_compile first
        install_lazy_compile()
        
        # Reset the compile method
        reset_compile()
        
        # Check if the original compile method is restored
        assert re.compile == original_compile, "Expected re.compile to be restored to its original state"
    
    finally:
        pass  # No need to restore anything as it was never changed