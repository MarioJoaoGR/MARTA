
import pytest
from unittest.mock import patch
from cli_mgr import CLIMgr

# Scenario 1: Test if CLI is available with valid input
def test_valid_input_cli_available():
    # Create a mock instance of CLIMgr with a valid CLI path
    cli_mgr = CLIMgr()
    cli_mgr.CLI = "valid_binary_path"
    
    # Test the is_available method
    assert cli_mgr.is_available(), "Expected True for valid input, but got False"

# Scenario 2: Test when CLI value is missing or None, expecting False return
def test_missing_cli_value():
    # Create a mock instance of CLIMgr with no CLI path set
    cli_mgr = CLIMgr()
    
    # Test the is_available method
    assert not cli_mgr.is_available(), "Expected False for missing or None CLI value, but got True"

# Scenario 3: Test error handling when get_bin_path raises ValueError, expecting False return
def test_error_handling_get_bin_path():
    # Create a mock instance of CLIMgr with a non-existent CLI path
    cli_mgr = CLIMgr()
    cli_mgr.CLI = "non_existent_binary_path"
    
    # Test the is_available method, which should raise ValueError and return False
    assert not cli_mgr.is_available(), "Expected False for error handling case, but got True"
