
import os
from pathlib import Path
from unittest.mock import patch, MagicMock

# Assuming the module 'httpie.config' has been imported correctly in your test file

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
    if is_windows():
        return DEFAULT_WINDOWS_CONFIG_DIR

    home_dir = Path.home()

    # 3. legacy ~/.httpie
    legacy_config_dir = home_dir / 'httpie'
    if legacy_config_dir.exists():
        return legacy_config_dir

    # 4. XDG
    xdg_config_home_dir = os.environ.get(
        'XDG_CONFIG_HOME',  # 4.1. explicit
        home_dir / '.config'  # 4.2. default
    )
    return Path(xdg_config_home_dir) / 'httpie'

# Test case for get_default_config_dir function
def test_get_default_config_dir():
    with patch('os.environ', {'HTTPIE_CONFIG_DIR': '/custom/path'}):
        assert str(get_default_config_dir()) == '/custom/path'

    with patch('os.environ', {}):
        assert str(get_default_config_dir()) == str(Path.home() / '.httpie')

    with patch('os.environ', {'XDG_CONFIG_HOME': '/custom/xdg'}):
        assert str(get_default_config_dir()) == '/custom/xdg/httpie'

    with patch('os.environ', {}):
        with patch('pathlib.Path.home', return_value=MagicMock(spec=Path)):
            home_mock = MagicMock()
            home_mock.__truediv__.return_value = Path('/home/user')
            with patch('pathlib.Path.home', return_value=home_mock):
                assert str(get_default_config_dir()) == '/home/user/.config/httpie'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_config_get_default_config_dir_1_test_error_case
httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_1_test_error_case.py:28:7: E0602: Undefined variable 'is_windows' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_1_test_error_case.py:29:15: E0602: Undefined variable 'DEFAULT_WINDOWS_CONFIG_DIR' (undefined-variable)


"""