
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

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___le___1.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_input _______________________________

    def test_valid_input():
        v1 = SemanticVersion('1.2.3')
        assert v1.major == 1
        assert v1.minor == 2
        assert v1.patch == 3
    
        v2 = SemanticVersion('1.0.0-alpha.1')
>       assert v2.prerelease == ('alpha', '1')
E       AssertionError: assert ('alpha', 1) == ('alpha', '1')
E         
E         At index 1 diff: 1 != '1'
E         Use -v to get more diff

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___le___1.py:12: AssertionError
______________________________ test_invalid_input ______________________________

    def test_invalid_input():
        with pytest.raises(ValueError):
            try:
>               SemanticVersion('invalid_version')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___le___1.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/version.py:145: in __init__
    self.parse(vstring)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = SemanticVersion('invalid_version'), vstring = 'invalid_version'

    def parse(self, vstring):
        match = SEMVER_RE.match(vstring)
        if not match:
>           raise ValueError("invalid semantic version '%s'" % vstring)
E           ValueError: invalid semantic version 'invalid_version'

/opt/marta/baselines/codamosa/replication/test-apps/ansible/lib/ansible/utils/version.py:194: ValueError

During handling of the above exception, another exception occurred:

    def test_invalid_input():
        with pytest.raises(ValueError):
            try:
                SemanticVersion('invalid_version')
            except ValueError as e:
>               assert str(e) == "Invalid version string 'invalid_version'"
E               assert "invalid sema...alid_version'" == "Invalid vers...alid_version'"
E                 
E                 - Invalid version string 'invalid_version'
E                 ? ^              -------
E                 + invalid semantic version 'invalid_version'
E                 ? ^      +++++++++

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___le___1.py:19: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___le___1.py::test_valid_input
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_utils_version_SemanticVersion___le___1.py::test_invalid_input
============================== 2 failed in 0.73s ===============================
"""