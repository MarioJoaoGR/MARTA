
import pytest
from isort._vendored.tomli._parser import parse_value, Pos

def test_valid_literal_string(parser):
    src = "'this is a test'"
    pos = Pos(0)
    updated_pos, parsed_str = parser(src, pos)
    assert isinstance(parsed_str, str)
    assert parsed_str == "this is a test"
    assert updated_pos.i == len(src)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_0_test_valid_literal_string.py E [100%]

==================================== ERRORS ====================================
_________________ ERROR at setup of test_valid_literal_string __________________
file /projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_0_test_valid_literal_string.py, line 5
  def test_valid_literal_string(parser):
E       fixture 'parser' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/projects/F202407648IACDCF2/mario/isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_0_test_valid_literal_string.py:5
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR isort/Test4DT_tests/test_isort__vendored_tomli__parser_parse_value_0_test_valid_literal_string.py::test_valid_literal_string
=============================== 1 error in 0.10s ===============================
"""