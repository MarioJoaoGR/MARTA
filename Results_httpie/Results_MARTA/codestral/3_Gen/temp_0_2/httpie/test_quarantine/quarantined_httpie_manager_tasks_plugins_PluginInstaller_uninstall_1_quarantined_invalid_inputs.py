
import pytest
from unittest.mock import patch, MagicMock
from httpie.manager.tasks.plugins import PluginInstaller, Environment, ExitStatus

def test_invalid_inputs():
    with patch('httpie.manager.tasks.plugins.Environment', autospec=True):
        env = Environment(config=MagicMock(), stderr=MagicMock())
        installer = PluginInstaller(env=env, debug=False)

        # Test with non-string values
        with pytest.raises(TypeError):
            installer.uninstall([123])  # Non-string value in targets list

        with pytest.raises(TypeError):
            installer.uninstall(["plugin1", None])  # NoneType in targets list

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

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_invalid_inputs.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        with patch('httpie.manager.tasks.plugins.Environment', autospec=True):
            env = Environment(config=MagicMock(), stderr=MagicMock())
            installer = PluginInstaller(env=env, debug=False)
    
            # Test with non-string values
            with pytest.raises(TypeError):
                installer.uninstall([123])  # Non-string value in targets list
    
            with pytest.raises(TypeError):
>               installer.uninstall(["plugin1", None])  # NoneType in targets list

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_invalid_inputs.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
httpie/httpie/manager/tasks/plugins.py:193: in uninstall
    exit_code |= self._uninstall(target) or ExitStatus.SUCCESS
httpie/httpie/manager/tasks/plugins.py:150: in _uninstall
    distribution = importlib_metadata.distribution(target)
/usr/local/lib/python3.11/importlib/metadata/__init__.py:982: in distribution
    return Distribution.from_name(distribution_name)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'importlib.metadata.Distribution'>, name = None

    @classmethod
    def from_name(cls, name: str):
        """Return the Distribution for the given package name.
    
        :param name: The name of the distribution package to search for.
        :return: The Distribution instance (or subclass thereof) for the named
            package, if found.
        :raises PackageNotFoundError: When the named package's distribution
            metadata cannot be found.
        :raises ValueError: When an invalid value is supplied for name.
        """
        if not name:
>           raise ValueError("A distribution name is required.")
E           ValueError: A distribution name is required.

/usr/local/lib/python3.11/importlib/metadata/__init__.py:561: ValueError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller_uninstall_1_test_invalid_inputs.py::test_invalid_inputs
============================== 1 failed in 0.26s ===============================
"""