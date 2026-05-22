
import os
from pathlib import Path
from unittest.mock import patch

# Assuming the function get_default_config_dir() and necessary constants are defined in httpie.config module
# from httpie.config import ENV_HTTPIE_CONFIG_DIR, DEFAULT_WINDOWS_CONFIG_DIR, DEFAULT_RELATIVE_LEGACY_CONFIG_DIR, ENV_XDG_CONFIG_HOME, DEFAULT_RELATIVE_XDG_CONFIG_HOME, DEFAULT_CONFIG_DIRNAME

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
    env_config_dir = os.environ.get('ENV_HTTPIE_CONFIG_DIR')
    if env_config_dir:
        return Path(env_config_dir)

    # 2. Windows
    if is_windows:
        return DEFAULT_WINDOWS_CONFIG_DIR

    home_dir = Path.home()

    # 3. legacy ~/.httpie
    legacy_config_dir = home_dir / 'DEFAULT_RELATIVE_LEGACY_CONFIG_DIR'
    if legacy_config_dir.exists():
        return legacy_config_dir

    # 4. XDG
    xdg_config_home_dir = os.environ.get(
        'ENV_XDG_CONFIG_HOME',  # 4.1. explicit
        home_dir / 'DEFAULT_RELATIVE_XDG_CONFIG_HOME'  # 4.2. default
    )
    return Path(xdg_config_home_dir) / 'DEFAULT_CONFIG_DIRNAME'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_config_get_default_config_dir_1_test_edge_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_get_default_config_dir_1_test_edge_case.py:29:7: E0602: Undefined variable 'is_windows' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_get_default_config_dir_1_test_edge_case.py:30:15: E0602: Undefined variable 'DEFAULT_WINDOWS_CONFIG_DIR' (undefined-variable)


"""