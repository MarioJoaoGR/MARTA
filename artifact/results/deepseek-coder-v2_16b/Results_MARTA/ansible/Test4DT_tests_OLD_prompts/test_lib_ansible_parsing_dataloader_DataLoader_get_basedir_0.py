
import pytest
from ansible.parsing.dataloader import DataLoader  # Replace 'your_module' with the actual module name where DataLoader is defined

# Test case for get_basedir method
def test_get_basedir():
    dl = DataLoader()
    assert dl.get_basedir() == '.'
