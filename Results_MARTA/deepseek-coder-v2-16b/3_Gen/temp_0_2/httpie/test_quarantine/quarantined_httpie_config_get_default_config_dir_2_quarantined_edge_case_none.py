
import os
from pathlib import Path
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

# Mocking the is_windows function for testing on non-Windows systems
def is_windows():
    mock_is_windows = MagicMock(return_value=False)
    with patch('os.name', new='posix'):
        return mock_is_windows()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_deepseek-coder-v2_16b.test_httpie_config_get_default_config_dir_2_test_edge_case_none
httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_config_get_default_config_dir_2_test_edge_case_none.py:27:15: E0602: Undefined variable 'DEFAULT_WINDOWS_CONFIG_DIR' (undefined-variable)


"""