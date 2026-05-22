
import pytest
from httpie.cli.argtypes import KeyValueArg

def test_valid_inputs():
    # Test valid key-value pairs with different separators
    kv1 = KeyValueArg("key", "value", ":", "key:value")
    assert kv1.key == "key"
    assert kv1.value == "value"
    assert kv1.sep == ":"
    assert kv1.orig == "key:value"

    kv2 = KeyValueArg("key", None, ":=", "key:=value")
    assert kv2.key == "key"
    assert kv2.value == "value"

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArg___repr___0_test_valid_inputs.py F [100%]

=================================== FAILURES ===================================
______________________________ test_valid_inputs _______________________________

    def test_valid_inputs():
        # Test valid key-value pairs with different separators
        kv1 = KeyValueArg("key", "value", ":", "key:value")
        assert kv1.key == "key"
        assert kv1.value == "value"
        assert kv1.sep == ":"
        assert kv1.orig == "key:value"
    
        kv2 = KeyValueArg("key", None, ":=", "key:=value")
        assert kv2.key == "key"
>       assert kv2.value == "value"
E       AssertionError: assert None == 'value'
E        +  where None = {'key': 'key', 'value': None, 'sep': ':=', 'orig': 'key:=value'}.value

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArg___repr___0_test_valid_inputs.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArg___repr___0_test_valid_inputs.py::test_valid_inputs
============================== 1 failed in 0.24s ===============================
"""