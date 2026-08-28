
import pytest
import argparse
from ansible.cli.arguments.option_helpers import add_async_options

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_async_options_2.py F [100%]

=================================== FAILURES ===================================
____________________________ test_add_async_options ____________________________

    def test_add_async_options():
        parser = argparse.ArgumentParser()
        add_async_options(parser)
    
        # Test default values
        args = parser.parse_args([])
        assert args.poll_interval == 15, f"Expected poll_interval to be 15 but got {args.poll_interval}"
        assert args.seconds == 0, f"Expected seconds to be 0 but got {args.seconds}"
    
        # Test setting specific values
>       with pytest.raises(SystemExit):
E       Failed: DID NOT RAISE <class 'SystemExit'>

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_async_options_2.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_async_options_2.py::test_add_async_options
============================== 1 failed in 0.99s ===============================
"""