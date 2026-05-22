
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

def test_as_site(mock_sysconfig):
    path = Path('/custom/python/installation')
    extra_vars = {'user': True}
    
    # Mock the sysconfig.get_path to return a specific site-packages path
    mock_sysconfig.return_value = '/specific/site-packages/path'
    
    result = as_site(path, **extra_vars)
    
    assert str(result) == '/specific/site-packages/path'
