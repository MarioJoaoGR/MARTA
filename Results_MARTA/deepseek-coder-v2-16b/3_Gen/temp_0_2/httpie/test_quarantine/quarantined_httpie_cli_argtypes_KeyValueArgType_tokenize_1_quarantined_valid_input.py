
import pytest
from httpie.cli.argtypes import KeyValueArgType, Escaped

def test_tokenize():
    key_value_parser = KeyValueArgType('\\=')
    tokens = key_value_parser.tokenize(r'foo\=bar\\baz')
    assert tokens == ['foo', Escaped('='), 'bar\\\\baz']

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArgType_tokenize_1_test_valid_input.py F [100%]

=================================== FAILURES ===================================
________________________________ test_tokenize _________________________________

    def test_tokenize():
        key_value_parser = KeyValueArgType('\\=')
        tokens = key_value_parser.tokenize(r'foo\=bar\\baz')
>       assert tokens == ['foo', Escaped('='), 'bar\\\\baz']
E       AssertionError: assert ['foo', Escap...('\\'), 'baz'] == ['foo', Escap... 'bar\\\\baz']
E         
E         At index 2 diff: 'bar' != 'bar\\\\baz'
E         Left contains 2 more items, first extra item: Escaped('\\')
E         Use -v to get more diff

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArgType_tokenize_1_test_valid_input.py:8: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArgType_tokenize_1_test_valid_input.py::test_tokenize
============================== 1 failed in 0.23s ===============================
"""