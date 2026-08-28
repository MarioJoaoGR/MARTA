
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
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___lt___0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________________ test_valid_version ______________________________

    def test_valid_version():
        v = SemanticVersion("1.2.3")
        assert v.major == 1
        assert v.minor == 2
        assert v.patch == 3
>       assert not hasattr(v, 'prerelease')
E       AssertionError: assert not True
E        +  where True = hasattr(SemanticVersion('1.2.3'), 'prerelease')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___lt___0.py:10: AssertionError
_________________________ test_version_with_prerelease _________________________

    def test_version_with_prerelease():
        v = SemanticVersion("1.0.0-alpha.1")
        assert v.major == 1
        assert v.minor == 0
        assert v.patch == 0
>       assert v.prerelease == ('alpha', '1')
E       AssertionError: assert ('alpha', 1) == ('alpha', '1')
E         
E         At index 1 diff: 1 != '1'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___lt___0.py:18: AssertionError
_______________________ test_version_with_buildmetadata ________________________

    def test_version_with_buildmetadata():
        v = SemanticVersion("1.0.0+build123")
        assert v.major == 1
        assert v.minor == 0
        assert v.patch == 0
>       assert not hasattr(v, 'prerelease')
E       AssertionError: assert not True
E        +  where True = hasattr(SemanticVersion('1.0.0+build123'), 'prerelease')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___lt___0.py:25: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___lt___0.py::test_valid_version
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___lt___0.py::test_version_with_prerelease
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___lt___0.py::test_version_with_buildmetadata
============================== 3 failed in 0.38s ===============================
"""