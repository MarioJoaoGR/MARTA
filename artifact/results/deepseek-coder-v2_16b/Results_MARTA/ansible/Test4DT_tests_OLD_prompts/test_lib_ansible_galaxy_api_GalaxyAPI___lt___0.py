
import pytest
from unittest.mock import patch
from ansible.galaxy.api import GalaxyAPI




def test_priority_same():
    api1 = GalaxyAPI(galaxy='a', name='b', url='c', priority=1)
    api2 = GalaxyAPI(galaxy='d', name='e', url='f', priority=1)
    
    assert (api1 < api2) == False  # Both should have the same priority, so it's not less than