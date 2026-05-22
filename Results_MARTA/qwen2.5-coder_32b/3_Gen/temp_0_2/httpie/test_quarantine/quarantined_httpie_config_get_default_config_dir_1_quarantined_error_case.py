
import os
from pathlib import Path
import pytest
from unittest.mock import patch, MagicMock

# Assuming the function get_default_config_dir() and constants are defined in httpie.config module
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
    if is_windows():
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

def is_windows():
    """Mockable function to check if the OS is Windows."""
    return os.name == 'nt'

# Mocking environment variables and system specifics for testing
@pytest.fixture(autouse=True)
def mock_env_vars(monkeypatch):
    monkeypatch.setenv('ENV_HTTPIE_CONFIG_DIR', '/custom/config')
    monkeypatch.setenv('ENV_XDG_CONFIG_HOME', '/home/user/.config')
    # Mocking is_windows function to return True for Windows OS (for testing on non-Windows systems)
    with patch('httpie.config.is_windows', return_value=False):
        yield

# Test case for get_default_config_dir()
def test_get_default_config_dir():
    # Case 1: Environment variable set
    os.environ['ENV_HTTPIE_CONFIG_DIR'] = '/custom/config'
    assert str(get_default_config_dir()) == '/custom/config'

    # Case 2: No environment variable set, Windows OS
    del os.environ['ENV_HTTPIE_CONFIG_DIR']
    with patch('httpie.config.is_windows', return_value=True):
        assert str(get_default_config_dir()) == DEFAULT_WINDOWS_CONFIG_DIR

    # Case 3: No environment variable set, non-Windows OS, legacy config exists
    del os.environ['ENV_HTTPIE_CONFIG_DIR']
    with patch('httpie.config.is_windows', return_value=False):
        (Path.home() / 'DEFAULT_RELATIVE_LEGACY_CONFIG_DIR').touch()
        assert str(get_default_config_dir()) == Path.home() / 'DEFAULT_RELATIVE_LEGACY_CONFIG_DIR'

    # Case 4: No environment variable set, non-Windows OS, no legacy config
    del os.environ['ENV_HTTPIE_CONFIG_DIR']
    with patch('httpie.config.is_windows', return_value=False):
        (Path.home() / 'DEFAULT_RELATIVE_LEGACY_CONFIG_DIR').unlink()
        assert str(get_default_config_dir()) == Path.home() / '.config/DEFAULT_CONFIG_DIRNAME'

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_qwen2.5-coder_32b.test_httpie_config_get_default_config_dir_1_test_error_case
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_get_default_config_dir_1_test_error_case.py:31:15: E0602: Undefined variable 'DEFAULT_WINDOWS_CONFIG_DIR' (undefined-variable)
httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_config_get_default_config_dir_1_test_error_case.py:69:48: E0602: Undefined variable 'DEFAULT_WINDOWS_CONFIG_DIR' (undefined-variable)


"""