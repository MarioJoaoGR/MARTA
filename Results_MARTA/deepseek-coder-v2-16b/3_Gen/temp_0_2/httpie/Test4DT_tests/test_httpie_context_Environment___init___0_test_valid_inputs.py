
import pytest
from httpie.context import Environment
import sys
from pathlib import Path
from unittest.mock import patch

@pytest.fixture(scope="function")
def valid_environment():
    return Environment(config_dir=Path('/tmp/config'))

def test_valid_inputs(valid_environment):
    assert valid_environment.config_dir == Path('/tmp/config')
