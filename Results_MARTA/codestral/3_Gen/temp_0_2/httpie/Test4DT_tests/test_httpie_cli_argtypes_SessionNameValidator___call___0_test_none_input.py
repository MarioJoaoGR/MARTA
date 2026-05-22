
import pytest
from unittest.mock import patch
from httpie.cli.argtypes import SessionNameValidator
import argparse

def test_none_input():
    validator = SessionNameValidator("Invalid session name.")
    
    with pytest.raises(argparse.ArgumentError) as excinfo:
        validator("")
        
    assert str(excinfo.value) == "Invalid session name."
