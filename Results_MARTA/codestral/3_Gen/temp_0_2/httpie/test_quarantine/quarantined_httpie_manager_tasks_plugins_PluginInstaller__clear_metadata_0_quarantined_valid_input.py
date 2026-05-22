
import pytest
from httpie.manager.tasks.plugins import PluginInstaller
from unittest.mock import patch, MagicMock
from pathlib import Path
import shutil
from collections import defaultdict

@pytest.fixture(autouse=True)
def mock_environment():
    env = MagicMock()
    env.config.plugins_dir = Path("/fake/plugin/directory")
    yield env

class TestPluginInstaller:
    @pytest.mark.parametrize("targets", [["plugin1-1.0"], ["plugin2-2.0"]])
    def test_valid_input(self, mock_environment, targets):
        with patch('httpie.manager.tasks.plugins._clear_metadata') as mock_clear_metadata:
            installer = PluginInstaller(env=mock_environment)
            installer._clear_metadata(targets)
            assert mock_clear_metadata.called

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________ TestPluginInstaller.test_valid_input[targets0] ________________

self = <Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.TestPluginInstaller object at 0x7fef1f9b3ed0>
mock_environment = <MagicMock id='140665027714768'>, targets = ['plugin1-1.0']

    @pytest.mark.parametrize("targets", [["plugin1-1.0"], ["plugin2-2.0"]])
    def test_valid_input(self, mock_environment, targets):
>       with patch('httpie.manager.tasks.plugins._clear_metadata') as mock_clear_metadata:

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fef1f9bbc90>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'httpie.manager.tasks.plugins' from '/projects/F202407648IACDCF2/mario/httpie/httpie/manager/tasks/plugins.py'> does not have the attribute '_clear_metadata'

/usr/local/lib/python3.11/unittest/mock.py:1419: AttributeError
________________ TestPluginInstaller.test_valid_input[targets1] ________________

self = <Test4DT_tests_codestral.test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.TestPluginInstaller object at 0x7fef1f9b8750>
mock_environment = <MagicMock id='140665011217744'>, targets = ['plugin2-2.0']

    @pytest.mark.parametrize("targets", [["plugin1-1.0"], ["plugin2-2.0"]])
    def test_valid_input(self, mock_environment, targets):
>       with patch('httpie.manager.tasks.plugins._clear_metadata') as mock_clear_metadata:

httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/usr/local/lib/python3.11/unittest/mock.py:1446: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7fef2042df90>

    def get_original(self):
        target = self.getter()
        name = self.attribute
    
        original = DEFAULT
        local = False
    
        try:
            original = target.__dict__[name]
        except (AttributeError, KeyError):
            original = getattr(target, name, DEFAULT)
        else:
            local = True
    
        if name in _builtins and isinstance(target, ModuleType):
            self.create = True
    
        if not self.create and original is DEFAULT:
>           raise AttributeError(
                "%s does not have the attribute %r" % (target, name)
            )
E           AttributeError: <module 'httpie.manager.tasks.plugins' from '/projects/F202407648IACDCF2/mario/httpie/httpie/manager/tasks/plugins.py'> does not have the attribute '_clear_metadata'

/usr/local/lib/python3.11/unittest/mock.py:1419: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.py::TestPluginInstaller::test_valid_input[targets0]
FAILED httpie/Test4DT_tests_codestral/test_httpie_manager_tasks_plugins_PluginInstaller__clear_metadata_0_test_valid_input.py::TestPluginInstaller::test_valid_input[targets1]
============================== 2 failed in 0.29s ===============================
"""