
import pytest
from ansible.module_utils.compat.version import StrictVersion



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_1.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_version ______________________________

    def test_valid_version():
        v1 = StrictVersion("1.2.3")
>       assert v1.major == 1
E       AttributeError: 'StrictVersion' object has no attribute 'major'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_1.py:7: AttributeError
_________________________ test_version_with_prerelease _________________________

    def test_version_with_prerelease():
        v2 = StrictVersion("0.5a1")
>       assert v2.major == 0
E       AttributeError: 'StrictVersion' object has no attribute 'major'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_1.py:14: AttributeError
_______________________ test_version_with_buildmetadata ________________________

    def test_version_with_buildmetadata():
        v3 = StrictVersion("1.0.4b1")
>       assert v3.major == 1
E       AttributeError: 'StrictVersion' object has no attribute 'major'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_1.py:21: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_1.py::test_valid_version
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_1.py::test_version_with_prerelease
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_1.py::test_version_with_buildmetadata
============================== 3 failed in 0.31s ===============================
"""