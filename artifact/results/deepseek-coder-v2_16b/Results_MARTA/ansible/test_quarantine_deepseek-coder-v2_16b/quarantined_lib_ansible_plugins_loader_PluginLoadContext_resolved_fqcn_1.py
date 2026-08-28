
import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import PluginLoadContext

# Test for missing lines in resolved_fqcn method
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_PluginLoadContext_resolved_fqcn_1.py F [100%]

=================================== FAILURES ===================================
______________________________ test_missing_lines ______________________________

    def test_missing_lines():
        ctx = PluginLoadContext()
        ctx.original_name = 'some_plugin'
        with pytest.raises(AnsibleError):
>           assert ctx.resolved_fqcn() is None
E           TypeError: 'NoneType' object is not callable

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_PluginLoadContext_resolved_fqcn_1.py:11: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_plugins_loader_PluginLoadContext_resolved_fqcn_1.py::test_missing_lines
============================== 1 failed in 0.74s ===============================
"""