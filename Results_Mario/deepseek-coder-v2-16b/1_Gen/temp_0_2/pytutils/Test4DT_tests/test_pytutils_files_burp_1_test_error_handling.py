
import pytest
import sys
import os
from pytutils.files import burp

@pytest.mark.parametrize("mode", ['r+'])
def test_error_handling(mode):
    with pytest.raises(IOError):
        # Test the scenario where an IOError should be raised for mode 'r+'
        burp('non_existent_file', 'test contents', mode=mode)
