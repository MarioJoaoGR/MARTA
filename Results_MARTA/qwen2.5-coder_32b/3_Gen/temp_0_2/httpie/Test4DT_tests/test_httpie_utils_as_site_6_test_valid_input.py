
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

def test_valid_input():
    with patch('sysconfig.get_path') as mock_get_path:
        mock_get_path.return_value = '/custom/python/installation/site-packages'
        
        result = as_site(Path('/custom/python/installation'))
        
        assert str(result) == '/custom/python/installation/site-packages'
