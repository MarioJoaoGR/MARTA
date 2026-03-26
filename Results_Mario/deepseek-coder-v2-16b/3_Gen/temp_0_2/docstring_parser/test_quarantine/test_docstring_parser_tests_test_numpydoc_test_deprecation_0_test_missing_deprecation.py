
import pytest
from docstring_parser.tests.test_numpydoc import parse  # Assuming the correct import path for `parse` function
import typing as T

def test_deprecation(
    source: str,
    expected_depr_version: T.Optional[str],
    expected_depr_desc: T.Optional[str],
) -> None:
    """Test parsing deprecation notes from a given source string and verify the parsed information against expected values."""
    docstring = parse(source)

    assert docstring.deprecation is not None, "Deprecation information not found."
    if expected_depr_version is not None:
        assert docstring.deprecation.version == expected_depr_version, f"Expected deprecation version {expected_depr_version} but got {docstring.deprecation.version}"
    if expected_depr_desc is not None:
        assert docstring.deprecation.description == expected_depr_desc, f"Expected deprecation description '{expected_depr_desc}' but got '{docstring.deprecation.description}'"

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py E [100%]

==================================== ERRORS ====================================
______________________ ERROR at setup of test_deprecation ______________________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py, line 6
  def test_deprecation(
E       fixture 'source' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py:6
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py::test_deprecation
=============================== 1 error in 0.03s ===============================
"""