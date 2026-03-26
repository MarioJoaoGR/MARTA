
from docstring_parser.tests.test_google import parse, compose, RenderingStyle
import pytest

@pytest.fixture
def source():
    return """Example Google-style docstring."""

def test_compose_clean(source, expected):
    assert (
        compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected
    )

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_1_test_invalid_input_error_handling.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_compose_clean _____________________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_1_test_invalid_input_error_handling.py, line 9
  def test_compose_clean(source, expected):
E       fixture 'expected' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, source, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_1_test_invalid_input_error_handling.py:9
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_1_test_invalid_input_error_handling.py::test_compose_clean
=============================== 1 error in 0.03s ===============================
"""