
import pytest
from httpie.cli.argtypes import KeyValueArgType, Escaped

@pytest.fixture
def key_value_parser():
    return KeyValueArgType()

def test_edge_case(key_value_parser):
    tokens = key_value_parser.tokenize('foo=bar')
    assert tokens == ['foo', '=', 'bar']

    tokens = key_value_parser.tokenize(r'foo\=bar')
    assert tokens == ['foo', Escaped('='), 'bar']

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

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_KeyValueArgType_tokenize_1_test_edge_case.py F [100%]

=================================== FAILURES ===================================
________________________________ test_edge_case ________________________________

key_value_parser = <httpie.cli.argtypes.KeyValueArgType object at 0x7fb6a01a3610>

    def test_edge_case(key_value_parser):
        tokens = key_value_parser.tokenize('foo=bar')
>       assert tokens == ['foo', '=', 'bar']
E       AssertionError: assert ['foo=bar'] == ['foo', '=', 'bar']
E         
E         At index 0 diff: 'foo=bar' != 'foo'
E         Right contains 2 more items, first extra item: '='
E         Use -v to get more diff

httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_KeyValueArgType_tokenize_1_test_edge_case.py:11: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
=========================== short test summary info ============================
FAILED httpie/Test4DT_tests_qwen2.5-coder_32b/test_httpie_cli_argtypes_KeyValueArgType_tokenize_1_test_edge_case.py::test_edge_case
============================== 1 failed in 0.24s ===============================
"""