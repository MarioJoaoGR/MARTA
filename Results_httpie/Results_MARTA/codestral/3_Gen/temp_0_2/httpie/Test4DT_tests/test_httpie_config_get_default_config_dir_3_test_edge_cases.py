
import os
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock

def get_default_config_dir() -> Path:
    """
    Return the path to the httpie configuration directory.

    This directory isn't guaranteed to exist, and nor are any of its
    ancestors (only the legacy ~/.httpie, if returned, is guaranteed to exist).

    XDG Base Directory Specification support:

        <https://wiki.archlinux.org/index.php/XDG_Base_Directory>

        $XDG_CONFIG_HOME is supported; $XDG_CONFIG_DIRS is not

    """
    # 1. explicitly set through env
    env_config_dir = os.environ.get('HTTPIE_CONFIG_DIR')
    if env_config_dir:
        return Path(env_config_dir)

    # 2. Windows
    if os.name == 'nt':
        return Path('C:\\ProgramData\\httpie')

    home_dir = Path.home()

    # 3. legacy ~/.httpie
    legacy_config_dir = home_dir / '.httpie'
    if legacy_config_dir.exists():
        return legacy_config_dir

    # 4. XDG
    xdg_config_home_dir = os.environ.get(
        'XDG_CONFIG_HOME',  # 4.1. explicit
        home_dir / '.config'  # 4.2. default
    )
    return Path(xdg_config_home_dir) / 'httpie'

@pytest.mark.skipif(os.name != 'nt', reason="This test is for Windows only")
def test_edge_cases():
    with patch('os.environ', {}):
        assert get_default_config_dir() == Path('C:\\ProgramData\\httpie')
    
    with patch('os.environ', {'HTTPIE_CONFIG_DIR': ''}):
        assert get_default_config_dir() == Path.home() / '.httpie'
