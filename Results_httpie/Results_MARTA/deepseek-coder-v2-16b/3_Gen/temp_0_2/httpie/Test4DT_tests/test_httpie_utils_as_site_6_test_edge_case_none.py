
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

@pytest.mark.parametrize("path, extra_vars, expected", [
    (Path('/custom/python/installation'), {}, Path('/custom/python/installation/lib/site-packages')),
    (Path('/custom/python/installation'), {'user': True}, Path('/custom/python/installation/lib/site-packages'))
])
def test_as_site(path, extra_vars, expected):
    with patch('sysconfig.get_path', return_value=str(expected)):
        result = as_site(path, **extra_vars)
        assert result == expected
