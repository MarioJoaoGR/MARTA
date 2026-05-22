
import pytest
from pathlib import Path
from httpie.utils import get_site_paths
from unittest.mock import patch

@pytest.fixture(scope="module")
def valid_path():
    return Path('/python/installations')

def test_valid_case(valid_path):
    with patch('httpie.compat.MIN_SUPPORTED_PY_VERSION', ('3', '7')):
        with patch('httpie.compat.MAX_SUPPORTED_PY_VERSION', ('3', '9')):
            paths = list(get_site_paths(valid_path))
            assert len(paths) > 0, "Expected at least one site-packages path"
