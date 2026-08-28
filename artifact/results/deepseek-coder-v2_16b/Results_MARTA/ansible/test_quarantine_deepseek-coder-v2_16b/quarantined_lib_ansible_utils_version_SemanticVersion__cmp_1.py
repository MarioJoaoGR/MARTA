
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion__cmp_1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
___________ test_semantic_version_creation_with_prerelease_and_build ___________

    def test_semantic_version_creation_with_prerelease_and_build():
        v = SemanticVersion("1.0.0-alpha.1")
>       assert v.prerelease == ('alpha', '1')
E       AssertionError: assert ('alpha', 1) == ('alpha', '1')
E         
E         At index 1 diff: 1 != '1'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion__cmp_1.py:7: AssertionError
___________ test_semantic_version_creation_with_specific_components ____________

    def test_semantic_version_creation_with_specific_components():
>       v = SemanticVersion(major=1, minor=2, patch=3, prerelease=('alpha', '1'), buildmetadata=('build', '123'))
E       TypeError: SemanticVersion.__init__() got an unexpected keyword argument 'major'

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion__cmp_1.py:10: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion__cmp_1.py::test_semantic_version_creation_with_prerelease_and_build
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion__cmp_1.py::test_semantic_version_creation_with_specific_components
============================== 2 failed in 0.38s ===============================
"""