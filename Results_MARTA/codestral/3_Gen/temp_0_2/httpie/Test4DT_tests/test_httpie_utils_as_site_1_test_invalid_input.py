
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

@pytest.mark.parametrize("invalid_input", [None, 123, "string"])
def test_invalid_input(invalid_input):
    with patch('sysconfig.get_path', MagicMock(side_effect=TypeError("Invalid input type"))):
        with pytest.raises(TypeError) as excinfo:
            as_site(Path('/fake/path'), **{'extra': 'vars'})
        assert str(excinfo.value) == "Invalid input type"
