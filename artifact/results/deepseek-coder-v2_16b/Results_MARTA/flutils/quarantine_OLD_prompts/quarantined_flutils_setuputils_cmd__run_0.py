
import pytest
from flutils.setuputils.cmd import SetupCfgCommandConfig
import subprocess
import sys
from unittest.mock import patch

def test_run_with_valid_commands():
    # Arrange
    commands = ("ls -l", "cd /tmp")
    config = SetupCfgCommandConfig(name="example_name", camel="example_camel", description="example_description", commands=commands)
    
    with patch('subprocess.run', return_value=0):  # Mock subprocess.run to always succeed
        with patch('sys.exit') as mock_exit:
            # Act
            config._run()
            
            # Assert
            assert len(config.commands) == 2
            for command in commands:
                print(f"Executing command: {command}")  # Ensure the command is printed
            mock_exit.assert_called_with(0)  # Ensure sys.exit was called with code 0

def test_run_with_invalid_commands():
    # Arrange
    commands = ("ls -l", "cd /nonexistent")
    config = SetupCfgCommandConfig(name="example_name", camel="example_camel", description="example_description", commands=commands)
    
    with patch('subprocess.run', side_effect=[None, subprocess.CalledProcessError(-1, 'cmd')]):  # Mock subprocess.run to fail the second command
        with patch('sys.exit') as mock_exit:
            # Act
            config._run()
            
            # Assert
            assert len(config.commands) == 2
            for i, command in enumerate(commands):
                if i == 1:  # Only the second command should be executed and fail
                    with pytest.raises(SystemExit) as exc_info:
                        print(f"Executing command: {command}")  # Ensure the command is printed
                    assert exc_info.value.code != 0
                else:
                    print(f"Executing command: {command}")  # Ensure the first command is printed and executed
            mock_exit.assert_called_with(1)  # Ensure sys.exit was called with code 1

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