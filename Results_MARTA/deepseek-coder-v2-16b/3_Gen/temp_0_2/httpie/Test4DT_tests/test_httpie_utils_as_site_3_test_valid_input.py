
import sysconfig
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock

def as_site(path: Path, **extra_vars) -> Path:
    site_packages_path = sysconfig.get_path(
        'purelib',
        vars={'base': str(path), **extra_vars}
    )
    return Path(site_packages_path)

@pytest.fixture
def mock_sysconfig():
    with patch('sysconfig.get_path') as mock_get_path:
        yield mock_get_path

def test_as_site_valid_input(mock_sysconfig):
    mock_get_path = MagicMock()
    mock_get_path.return_value = '/expected/site-packages'
    mock_sysconfig.side_effect = mock_get_path

    result = as_site(Path('/custom/python/installation'))
    assert str(result) == '/expected/site-packages'
