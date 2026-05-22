
import os
from pathlib import Path
from unittest.mock import patch

# Assuming the module 'httpie.config' has been imported correctly and contains necessary constants like ENV_HTTPIE_CONFIG_DIR, DEFAULT_WINDOWS_CONFIG_DIR, etc.

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
    with patch('httpie.config.is_windows', True):
        if httpie.config.is_windows:
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_config_get_default_config_dir_1_test_edge_case
httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_1_test_edge_case.py:29:11: E0602: Undefined variable 'httpie' (undefined-variable)
httpie/Test4DT_tests_codestral/test_httpie_config_get_default_config_dir_1_test_edge_case.py:30:19: E0602: Undefined variable 'DEFAULT_WINDOWS_CONFIG_DIR' (undefined-variable)


"""