
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

def test_invalid_input():
    with patch('sysconfig.get_path') as mock_get_path:
        # Mock the behavior of sysconfig.get_path to raise an error for invalid input
        mock_get_path.side_effect = ValueError("Invalid path")
        
        # Test that as_site raises a ValueError when given an invalid path
        with pytest.raises(ValueError):
            result = as_site(Path('/invalid/path'))
