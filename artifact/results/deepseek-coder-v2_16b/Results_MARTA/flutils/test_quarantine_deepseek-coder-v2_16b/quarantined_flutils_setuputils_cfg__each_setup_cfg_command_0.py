
from configparser import ConfigParser
import pytest
from flutils.setuputils.cfg import SetupCfgCommandConfig, _each_setup_cfg_command

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_setuputils_cfg__each_setup_cfg_command_0.py F [100%]

=================================== FAILURES ===================================
_________________________ test_each_setup_cfg_command __________________________

    def test_each_setup_cfg_command():
        parser = ConfigParser()
        parser['build'] = {'name': 'Build', 'description': 'Build the project', 'command': 'python setup.py build'}
        parser['install'] = {'name': 'Install', 'description': 'Install the project', 'commands': 'python setup.py install\npython another_script.py install'}
    
        format_kwargs = {'name': 'your_project'}
        expected_output = [
            SetupCfgCommandConfig('build', 'Build', 'Build the project', ('python setup.py build',)),
            SetupCfgCommandConfig('install', 'Install', 'Install the project', ('python setup.py install', 'python another_script.py install'))
        ]
    
        result = list(_each_setup_cfg_command(parser, format_kwargs))
>       assert len(result) == 2
E       assert 0 == 2
E        +  where 0 = len([])

/opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_setuputils_cfg__each_setup_cfg_command_0.py:18: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/flutils/Test4DT_tests_deepseek-coder-v2_16b/test_flutils_setuputils_cfg__each_setup_cfg_command_0.py::test_each_setup_cfg_command
============================== 1 failed in 0.13s ===============================
"""