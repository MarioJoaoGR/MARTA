
import argparse
import pytest
from ansible.cli.arguments.option_helpers import add_output_options

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_output_options_1.py F [100%]

=================================== FAILURES ===================================
_____________________________ test_invalid_inputs ______________________________

    def test_invalid_inputs():
        parser = argparse.ArgumentParser(prog='__main__.py', usage=None, description='Example script with output options', formatter_class=argparse.HelpFormatter, conflict_handler='error', add_help=True)
        add_output_options(parser)
    
        with pytest.raises(SystemExit) as e:
            parser.parse_args(['-x'])
    
>       assert str(e.value) == "usage: __main__.py [-h] [-o] [-t TREE]"
E       AssertionError: assert '2' == 'usage: __mai...-o] [-t TREE]'
E         
E         - usage: __main__.py [-h] [-o] [-t TREE]
E         + 2

/opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_output_options_1.py:13: AssertionError
----------------------------- Captured stderr call -----------------------------
usage: __main__.py [-h] [-o] [-t TREE]
__main__.py: error: unrecognized arguments: -x
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/ansible/Test4DT_tests_deepseek-coder-v2_16b/test_lib_ansible_cli_arguments_option_helpers_add_output_options_1.py::test_invalid_inputs
============================== 1 failed in 0.61s ===============================
"""