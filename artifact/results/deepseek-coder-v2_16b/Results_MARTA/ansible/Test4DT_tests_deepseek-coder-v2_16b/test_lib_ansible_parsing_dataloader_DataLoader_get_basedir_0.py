
import pytest
from ansible.parsing.dataloader import DataLoader

def test_get_basedir():
    dl = DataLoader()
    assert dl.get_basedir() == '.'
