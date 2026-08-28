
import pytest
from unittest.mock import patch
from thefuck.rules.choco_install import match
from thefuck.types import Command

@pytest.mark.parametrize("script, output, expected", [
    ('choco install', 'Installing the following packages', True),
    ('cinst', 'Installing the following packages', True),
    ('npm install', 'Package installation completed successfully', False)
])
def test_match(script, output, expected):
    command = Command(script=script, output=output)
    assert match(command) == expected
