
import pytest
from pathlib import Path
from unittest.mock import patch
from httpie.plugins.manager import PluginManager

def test_invalid_directory():
    pm = PluginManager()
    with patch('sys.path', []):  # Ensure no paths are added to sys.path
        with pytest.raises(FileNotFoundError):
            pm.load_installed_plugins(Path('/nonexistent/path'))

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_load_installed_plugins_4_test_invalid_directory.py F [100%]

=================================== FAILURES ===================================
____________________________ test_invalid_directory ____________________________

    def test_invalid_directory():
        pm = PluginManager()
        with patch('sys.path', []):  # Ensure no paths are added to sys.path
            with pytest.raises(FileNotFoundError):
>               pm.load_installed_plugins(Path('/nonexistent/path'))

httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_load_installed_plugins_4_test_invalid_directory.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/plugins/manager.py:67: in load_installed_plugins
    for entry_point in self.iter_entry_points(directory):
httpie/httpie/plugins/manager.py:60: in iter_entry_points
    with enable_plugins(directory):
/usr/local/lib/python3.11/contextlib.py:137: in __enter__
    return next(self.gen)
httpie/httpie/plugins/manager.py:29: in _load_directories
    plugin_dirs = [
httpie/httpie/plugins/manager.py:29: in <listcomp>
    plugin_dirs = [
httpie/httpie/utils.py:245: in get_site_paths
    yield as_site(path)
httpie/httpie/utils.py:222: in as_site
    site_packages_path = sysconfig.get_path(
/usr/local/lib/python3.11/sysconfig.py:626: in get_path
    return get_paths(scheme, vars, expand)[name]
/usr/local/lib/python3.11/sysconfig.py:616: in get_paths
    return _expand_vars(scheme, vars)
/usr/local/lib/python3.11/sysconfig.py:265: in _expand_vars
    _extend_dict(vars, get_config_vars())
/usr/local/lib/python3.11/sysconfig.py:670: in get_config_vars
    _init_posix(_CONFIG_VARS)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

vars = {'abiflags': '', 'base': '/usr/local', 'exec_prefix': '/usr/local', 'installed_base': '/usr/local', ...}

    def _init_posix(vars):
        """Initialize the module as appropriate for POSIX systems."""
        # _sysconfigdata is generated at build time, see _generate_posix_vars()
        name = _get_sysconfigdata_name()
>       _temp = __import__(name, globals(), locals(), ['build_time_vars'], 0)
E       ModuleNotFoundError: No module named '_sysconfigdata__linux_x86_64-linux-gnu'

/usr/local/lib/python3.11/sysconfig.py:531: ModuleNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_plugins_manager_PluginManager_load_installed_plugins_4_test_invalid_directory.py::test_invalid_directory
============================== 1 failed in 0.21s ===============================
"""