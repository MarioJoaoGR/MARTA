
import pytest
from ansible.utils.version import SemanticVersion


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___eq___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
____________________ test_semantic_version_with_prerelease _____________________

    def test_semantic_version_with_prerelease():
        v2 = SemanticVersion("1.0.0-alpha.1")
>       assert v2.prerelease == ('alpha', '1')
E       AssertionError: assert ('alpha', 1) == ('alpha', '1')
E         
E         At index 1 diff: 1 != '1'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___eq___0.py:7: AssertionError
___________________ test_semantic_version_with_buildmetadata ___________________

    def test_semantic_version_with_buildmetadata():
        v3 = SemanticVersion("1.0.0+build123")
>       assert v3.buildmetadata == ('build', '123')
E       AssertionError: assert ('build123',) == ('build', '123')
E         
E         At index 0 diff: 'build123' != 'build'
E         Right contains one more item: '123'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___eq___0.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___eq___0.py::test_semantic_version_with_prerelease
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___eq___0.py::test_semantic_version_with_buildmetadata
============================== 2 failed in 0.37s ===============================
"""