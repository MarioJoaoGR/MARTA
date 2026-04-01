
import pytest
from docstring_parser.tests.test_epydoc import parse

@pytest.fixture
def expected_short_desc():
    return "This is a test."

@pytest.fixture
def expected_long_desc():
    return "Description of argument 1.\nResult of the operation."

@pytest.fixture
def expected_blank():
    return True

def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
    """Test parsing long description."""
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank
    assert not docstring.meta

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_long_description_0_test_valid_input.py E [100%]

==================================== ERRORS ====================================
___________________ ERROR at setup of test_long_description ____________________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_long_description_0_test_valid_input.py, line 17
  def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
E       fixture 'source' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, expected_blank, expected_long_desc, expected_short_desc, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_long_description_0_test_valid_input.py:17
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_long_description_0_test_valid_input.py::test_long_description
=============================== 1 error in 0.03s ===============================
"""