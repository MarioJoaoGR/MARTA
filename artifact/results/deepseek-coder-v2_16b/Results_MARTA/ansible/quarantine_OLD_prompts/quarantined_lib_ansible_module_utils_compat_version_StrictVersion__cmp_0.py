
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
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_0.py F [100%]

=================================== FAILURES ===================================
________________________ test_edge_cases_strict_version ________________________

    def test_edge_cases_strict_version():
        with pytest.raises(ValueError):
            StrictVersion("1.3.a4")  # Invalid version string
>       assert StrictVersion("1.0.4a3") == StrictVersion("1.0.4b1"), "Pre-release tags comparison failed"
E       AssertionError: Pre-release tags comparison failed
E       assert StrictVersion ('1.0.4a3') == StrictVersion ('1.0.4b1')
E        +  where StrictVersion ('1.0.4a3') = StrictVersion('1.0.4a3')
E        +  and   StrictVersion ('1.0.4b1') = StrictVersion('1.0.4b1')

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_0.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_module_utils_compat_version_StrictVersion__cmp_0.py::test_edge_cases_strict_version
============================== 1 failed in 0.25s ===============================
"""