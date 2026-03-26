
import pytest
from docstring_parser.tests.test_numpydoc import parse  # Correctly importing from the specified module

@pytest.fixture(name="source")
def fixture_source():
    return "def func(arg1=5): pass"

def test_default_args(source, expected_is_optional, expected_type_name, expected_default):
    """Test parsing default arguments."""
    docstring = parse(source)
    assert docstring is not None
    assert len(docstring.params) == 1

    arg1 = docstring.params[0]
    assert arg1.is_optional == expected_is_optional
    assert arg1.type_name == expected_type_name
    assert arg1.default == expected_default

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_invalid_inputs.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_default_args ______________________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_invalid_inputs.py, line 9
  def test_default_args(source, expected_is_optional, expected_type_name, expected_default):
E       fixture 'expected_is_optional' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, source, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_invalid_inputs.py:9
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_default_args_0_test_invalid_inputs.py::test_default_args
=============================== 1 error in 0.03s ===============================
"""