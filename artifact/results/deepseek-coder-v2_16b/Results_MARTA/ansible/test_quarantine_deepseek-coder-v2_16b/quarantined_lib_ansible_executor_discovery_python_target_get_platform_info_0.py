
import pytest
from unittest.mock import patch, Mock
import platform as py_platform

def get_platform_info():
    result = dict(platform_dist_result=[])

    if hasattr(py_platform, 'dist'):
        result['platform_dist_result'] = py_platform.dist()

    osrelease_content = read_utf8_file('/etc/os-release')
    # try to fall back to /usr/lib/os-release
    if not osrelease_content:
        osrelease_content = read_utf8_file('/usr/lib/os-release')

    result['osrelease_content'] = osrelease_content

    return result


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_discovery_python_target_get_platform_info_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
______________________________ test_missing_files ______________________________

    def test_missing_files():
        with patch('os.path.exists', return_value=False):
>           info = get_platform_info()

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_discovery_python_target_get_platform_info_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

    def get_platform_info():
        result = dict(platform_dist_result=[])
    
        if hasattr(py_platform, 'dist'):
            result['platform_dist_result'] = py_platform.dist()
    
>       osrelease_content = read_utf8_file('/etc/os-release')
E       NameError: name 'read_utf8_file' is not defined

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_discovery_python_target_get_platform_info_0.py:12: NameError
__________________________ test_platform_dist_missing __________________________

    def test_platform_dist_missing():
>       with patch.object(py_platform, 'dist', Mock(side_effect=AttributeError)):

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_discovery_python_target_get_platform_info_0.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1447: in __enter__
    original, local = self.get_original()
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <unittest.mock._patch object at 0x7f9e123490f0>

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
E           AttributeError: <module 'platform' from '/opt/conda/envs/test4py_env/lib/python3.10/platform.py'> does not have the attribute 'dist'

/opt/conda/envs/test4py_env/lib/python3.10/unittest/mock.py:1420: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_discovery_python_target_get_platform_info_0.py::test_missing_files
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_executor_discovery_python_target_get_platform_info_0.py::test_platform_dist_missing
============================== 2 failed in 0.16s ===============================
"""