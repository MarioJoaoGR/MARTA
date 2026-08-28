
import pytest
from configparser import ConfigParser
from typing import Generator, Tuple, cast

def _each_setup_cfg_command_section(parser: ConfigParser) -> Generator[Tuple[str, str], None, None]:
    for section in parser.sections():
        if section.startswith('setup.command.'):
            command_name = '.'.join(section.split('.')[2:])
            yield section, command_name

def test_each_setup_cfg_command_section_basic():
    cfg_parser = ConfigParser()
    cfg_parser['setup.command.build'] = {'command': 'python setup.py build'}
    cfg_parser['setup.command.install'] = {'command': 'python setup.py install'}
    
    expected_output = [('setup.command.build', 'build'), ('setup.command.install', 'install')]
    result = list(_each_setup_cfg_command_section(cfg_parser))
    
    assert result == expected_output

def test_each_setup_cfg_command_section_no_sections():
    cfg_parser = ConfigParser()
    
    result = list(_each_setup_cfg_command_section(cfg_parser))
    
    assert not result, "Expected an empty generator since there are no sections"

def test_each_setup_cfg_command_section_real_config():
    cfg_parser = ConfigParser()
    cfg_parser.read('tests/test_setup.cfg')  # Assuming the configuration file is named 'test_setup.cfg'
    
    expected_output = [('setup.command.build', 'build'), ('setup.command.install', 'install')]
    result = list(_each_setup_cfg_command_section(cfg_parser))
    
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