
import pytest
from unittest.mock import patch
from thefuck.shells.generic import Generic

def test_get_aliases():
    generic_shell = Generic()
    assert generic_shell.get_aliases() == {}
