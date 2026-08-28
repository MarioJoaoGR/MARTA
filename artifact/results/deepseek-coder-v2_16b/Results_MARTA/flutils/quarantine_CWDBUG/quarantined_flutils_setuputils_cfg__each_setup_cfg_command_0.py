
import pytest
from configparser import ConfigParser
from your_module import _each_setup_cfg_command, SetupCfgCommandConfig
from typing import Dict, List, Generator

# Assuming 'your_module' is the module containing the function under test.
# Replace with the actual module name if different.

def test_each_setup_cfg_command_basic():
    parser = ConfigParser()
    parser['build'] = {'name': 'Build', 'command': 'python setup.py build'}
    parser['install'] = {'name': 'Install', 'command': 'python setup.py install'}
    
    format_kwargs = {'name': 'your_project'}
    
    expected_output = [
        SetupCfgCommandConfig('build', 'Build', '', ('python setup.py build',)),
        SetupCfgCommandConfig('install', 'Install', '', ('python setup.py install',))
    ]
    
    result = list(_each_setup_cfg_command(parser, format_kwargs))
    assert result == expected_output

def test_each_setup_cfg_command_custom_format():
    parser = ConfigParser()
    parser['build'] = {'name': 'Build', 'command': 'python setup.py build'}
    parser['install'] = {'name': 'Install', 'command': 'python setup.py install'}
    
    format_kwargs = {'name': 'custom_project'}
    
    expected_output = [
        SetupCfgCommandConfig('build', 'Build', '', ('python setup.py build',)),
        SetupCfgCommandConfig('install', 'Install', '', ('python setup.py install',))
    ]
    
    result = list(_each_setup_cfg_command(parser, format_kwargs))
    assert result == expected_output

def test_each_setup_cfg_command_no_name():
    parser = ConfigParser()
    parser['build'] = {'command': 'python setup.py build'}
    parser['install'] = {'command': 'python setup.py install'}
    
    format_kwargs = {'name': 'your_project'}
    
    expected_output = [
        SetupCfgCommandConfig('build', 'Build', '', ('python setup.py build',)),
        SetupCfgCommandConfig('install', 'Install', '', ('python setup.py install',))
    ]
    
    result = list(_each_setup_cfg_command(parser, format_kwargs))
    assert result == expected_output

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
Traceback (most recent call last):
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/opt/conda/envs/test4py_env/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/data/pydeps/marta/pytest/__main__.py", line 9, in <module>
    raise SystemExit(pytest.console_main())
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 201, in console_main
    code = main()
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 156, in main
    config = _prepareconfig(args, plugins)
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 332, in _prepareconfig
    config = get_config(args, plugins)
  File "/data/pydeps/marta/_pytest/config/__init__.py", line 293, in get_config
    dir=pathlib.Path.cwd(),
  File "/opt/conda/envs/test4py_env/lib/python3.10/pathlib.py", line 993, in cwd
    return cls(cls._accessor.getcwd())
FileNotFoundError: [Errno 2] No such file or directory
"""