
import pytest
from ansible.cli.doc import DocCLI

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_1.py F [100%]

=================================== FAILURES ===================================
__________________________ test_format_version_added ___________________________

    def test_format_version_added():
        # Test basic version added information
        assert DocCLI._format_version_added('2.9') == 'version 2.9'
    
        # Test with collection information
        assert DocCLI._format_version_added('3.0', 'ansible.builtin') == 'version 3.0 of ansible-core'
    
        # Test historical version added information
>       assert DocCLI._format_version_added('historical') == 'historical'
E       AssertionError: assert 'version historical' == 'historical'
E         
E         - historical
E         + version historical

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_1.py:13: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_doc_DocCLI__format_version_added_1.py::test_format_version_added
============================== 1 failed in 0.90s ===============================
"""