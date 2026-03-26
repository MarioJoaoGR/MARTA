
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS
import typing as T

def test_valid_input_default_settings(parser):
    assert isinstance(parser.sections, dict)
    # The default number of sections should be 5 based on the provided documentation and implementation
    assert len(parser.sections) == 5

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__setup_0_test_valid_input_default_settings.py E [100%]

==================================== ERRORS ====================================
_____________ ERROR at setup of test_valid_input_default_settings ______________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__setup_0_test_valid_input_default_settings.py, line 6
  def test_valid_input_default_settings(parser):
E       fixture 'parser' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__setup_0_test_valid_input_default_settings.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__setup_0_test_valid_input_default_settings.py::test_valid_input_default_settings
=============================== 1 error in 0.02s ===============================
"""