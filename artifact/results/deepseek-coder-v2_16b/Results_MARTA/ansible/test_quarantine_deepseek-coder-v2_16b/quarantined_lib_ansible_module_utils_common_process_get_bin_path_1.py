
import pytest
from ansible.module_utils.common.process import get_bin_path
import os

def is_executable(path):
    return os.access(path, os.X_OK)

@pytest.mark.parametrize("arg, opt_dirs, expected", [
    ('ls', None, 'Failed to find required executable "ls" in paths:'),
    ('ls', ['/custom/bin'], 'Failed to find required executable "ls" in paths:')
])
def test_get_bin_path_invalid(arg, opt_dirs, expected):
    with pytest.raises(ValueError) as excinfo:
        get_bin_path(arg, opt_dirs=opt_dirs)
    assert str(excinfo.value) == expected + os.pathsep.join(['/usr/local/sbin', '/usr/sbin', '/sbin'] + (['/custom/bin'] if opt_dirs else []))

@pytest.mark.parametrize("arg, required", [('ls', True), ('ls', None)])
def test_invalid_input_required_deprecated(arg, required):
    with pytest.raises(ValueError) as excinfo:
        get_bin_path(arg, required=required)
    assert str(excinfo.value).startswith('Failed to find required executable "')
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_ test_get_bin_path_invalid[ls-None-Failed to find required executable "ls" in paths:] _

arg = 'ls', opt_dirs = None
expected = 'Failed to find required executable "ls" in paths:'

    @pytest.mark.parametrize("arg, opt_dirs, expected", [
        ('ls', None, 'Failed to find required executable "ls" in paths:'),
        ('ls', ['/custom/bin'], 'Failed to find required executable "ls" in paths:')
    ])
    def test_get_bin_path_invalid(arg, opt_dirs, expected):
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py:14: Failed
_ test_get_bin_path_invalid[ls-opt_dirs1-Failed to find required executable "ls" in paths:] _

arg = 'ls', opt_dirs = ['/custom/bin']
expected = 'Failed to find required executable "ls" in paths:'

    @pytest.mark.parametrize("arg, opt_dirs, expected", [
        ('ls', None, 'Failed to find required executable "ls" in paths:'),
        ('ls', ['/custom/bin'], 'Failed to find required executable "ls" in paths:')
    ])
    def test_get_bin_path_invalid(arg, opt_dirs, expected):
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py:14: Failed
_______________ test_invalid_input_required_deprecated[ls-True] ________________

arg = 'ls', required = True

    @pytest.mark.parametrize("arg, required", [('ls', True), ('ls', None)])
    def test_invalid_input_required_deprecated(arg, required):
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py:20: Failed
_______________ test_invalid_input_required_deprecated[ls-None] ________________

arg = 'ls', required = None

    @pytest.mark.parametrize("arg, required", [('ls', True), ('ls', None)])
    def test_invalid_input_required_deprecated(arg, required):
>       with pytest.raises(ValueError) as excinfo:
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py:20: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py::test_get_bin_path_invalid[ls-None-Failed to find required executable "ls" in paths:]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py::test_get_bin_path_invalid[ls-opt_dirs1-Failed to find required executable "ls" in paths:]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py::test_invalid_input_required_deprecated[ls-True]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_common_process_get_bin_path_1.py::test_invalid_input_required_deprecated[ls-None]
============================== 4 failed in 0.32s ===============================
"""