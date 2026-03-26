
import pytest
from docstring_parser.tests.test_google import parse

@pytest.fixture(scope="module")
def source():
    return """
    def example():
        \"\"\"
        This is a summary.
        
        Args:
            arg1 (int): The first argument.
            arg2 (str): The second argument.
            
        Returns:
            int: The result of the function.
        \"\"\"
    """

def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc):
    docstring = parse(source)
    assert docstring.short_description == expected_short_desc
    assert docstring.long_description == expected_long_desc
    assert docstring.blank_after_short_description == expected_blank_short_desc
    assert docstring.blank_after_long_description == expected_blank_long_desc
    assert len(docstring.meta) == 1

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_edge_case.py E [100%]

==================================== ERRORS ====================================
_____________________ ERROR at setup of test_meta_newlines _____________________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_edge_case.py, line 21
  def test_meta_newlines(source, expected_short_desc, expected_long_desc, expected_blank_short_desc, expected_blank_long_desc):
E       fixture 'expected_short_desc' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, source, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_edge_case.py:21
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_meta_newlines_0_test_edge_case.py::test_meta_newlines
=============================== 1 error in 0.03s ===============================
"""