
import os
import sys
import pytest
from ansible.utils.py3compat import _TextEnviron


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_py3compat__TextEnviron___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________________ test_specific_encoding ____________________________

    def test_specific_encoding():
        utf8_env = _TextEnviron(encoding='utf-8')
        assert utf8_env.encoding == 'utf-8'
>       assert isinstance(utf8_env._raw_environ, dict)
E       AssertionError: assert False
E        +  where False = isinstance(environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '..., 'PYTEST_CURRENT_TEST': 'test_lib_ansible_utils_py3compat__TextEnviron___init___0.py::test_specific_encoding (call)'}), dict)
E        +    where environ({'SHELL': '/bin/bash', 'NV_LIBCUBLAS_VERSION': '12.4.5.8-1', 'NVIDIA_VISIBLE_DEVICES': 'all', 'WARP_IS_SSH': '..., 'PYTEST_CURRENT_TEST': 'test_lib_ansible_utils_py3compat__TextEnviron___init___0.py::test_specific_encoding (call)'}) = <ansible.utils.py3compat._TextEnviron object at 0x7f6d1011a020>._raw_environ

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_py3compat__TextEnviron___init___0.py:10: AssertionError
____________________________ test_none_environment _____________________________

    def test_none_environment():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_py3compat__TextEnviron___init___0.py:13: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_py3compat__TextEnviron___init___0.py::test_specific_encoding
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_py3compat__TextEnviron___init___0.py::test_none_environment
============================== 2 failed in 0.33s ===============================
"""