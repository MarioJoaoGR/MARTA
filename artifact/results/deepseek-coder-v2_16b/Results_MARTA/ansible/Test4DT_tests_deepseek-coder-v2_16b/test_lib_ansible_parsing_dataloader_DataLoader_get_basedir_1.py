
import pytest
from ansible.parsing.dataloader import DataLoader  # Import the correct module

# Test case for get_basedir method
def test_get_basedir():
    dl = DataLoader()
    assert dl.get_basedir() == '.'
