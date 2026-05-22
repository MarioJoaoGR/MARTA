
import pytest
from httpie.cli.options import drop_keys
from typing import Dict, Any, Tuple

def test_none_input():
    config = None
    blacklist = ('a',)
    with pytest.raises(TypeError):
        drop_keys(config, blacklist)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

httpie/Test4DT_tests_codestral/test_httpie_cli_options_drop_keys_1_test_none_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_none_input ________________________________

    def test_none_input():
        config = None
        blacklist = ('a',)
        with pytest.raises(TypeError):
>           drop_keys(config, blacklist)

httpie/Test4DT_tests_codestral/test_httpie_cli_options_drop_keys_1_test_none_input.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

configuration = None, key_blacklist = ('a',)

    def drop_keys(
        configuration: Dict[str, Any], key_blacklist: Tuple[str, ...]
    ):
        return {
            key: value
>           for key, value in configuration.items()
            if key not in key_blacklist
        }
E       AttributeError: 'NoneType' object has no attribute 'items'

httpie/httpie/cli/options.py:33: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_codestral/test_httpie_cli_options_drop_keys_1_test_none_input.py::test_none_input
============================== 1 failed in 0.18s ===============================
"""