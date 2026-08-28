
import pytest
from thefuck.rules.git_rm_recursive import match
from thefuck.types import Command



def test_error_case():
    command = Command(script='ls -l', output='some output')
    assert match(command) is False