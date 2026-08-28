
import pytest
from thefuck.shells import Generic

def test_how_to_configure():
    generic = Generic()
    assert generic.friendly_name == 'Generic Shell'
