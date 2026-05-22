
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

def test_as_site():
    with patch('sysconfig.get_path') as mock_get_path:
        mock_get_path.return_value = '/mocked/site-packages'
        
        path = Path('/custom/python/installation')
        result = as_site(path, user=True)
        
        assert str(result) == '/mocked/site-packages'
        mock_get_path.assert_called_once_with('purelib', vars={'base': '/custom/python/installation', 'user': True})
