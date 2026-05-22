
import pytest
from httpie.cli.argtypes import KeyValueArgType, KeyValueArg

def test_valid_input_happy_path(key_value_parser):
    kv_pair = key_value_parser('foo=bar')
    assert isinstance(kv_pair, KeyValueArg)
    assert kv_pair.key == 'foo'
    assert kv_pair.value == 'bar'

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

httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArgType___call___3_test_valid_input_happy_path.py E [100%]

==================================== ERRORS ====================================
________________ ERROR at setup of test_valid_input_happy_path _________________
file /projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArgType___call___3_test_valid_input_happy_path.py, line 5
  def test_valid_input_happy_path(key_value_parser):
E       fixture 'key_value_parser' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArgType___call___3_test_valid_input_happy_path.py:5
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR httpie/Test4DT_tests_deepseek-coder-v2_16b/test_httpie_cli_argtypes_KeyValueArgType___call___3_test_valid_input_happy_path.py::test_valid_input_happy_path
=============================== 1 error in 0.22s ===============================
"""