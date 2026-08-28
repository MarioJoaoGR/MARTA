# Module: thefuck.shells.generic
import pytest
from thefuck.shells.generic import Generic

@pytest.fixture
def generic_shell():
    return Generic()

def test_app_alias_thefuck(generic_shell):
    assert generic_shell.app_alias('thefuck') == 'alias thefuck=\'eval "$(TF_ALIAS=thefuck PYTHONIOENCODING=utf-8 thefuck "$(fc -ln -1)")"\''
