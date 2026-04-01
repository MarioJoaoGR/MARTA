
import pytest
from docstring_parser.tests.test_google import compose, parse, RenderingStyle

@pytest.fixture(params=[
    ("Parameters:\n- param1 (int): Description of param1\n- param2 (str): Description of param2", "Parameters:\n- param1: Description of param1\n- param2: Description of param2"),
    ("Returns:\n- return_value (bool): The result of the operation", "Returns:\n- return_value: The result of the operation")
])
def source_expected_pairs(request):
    return request.param

def test_compose_clean(source_expected_pairs, expected):
    source, expected = source_expected_pairs
    assert compose(parse(source), rendering_style=RenderingStyle.CLEAN) == expected

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform darwin -- Python 3.10.19, pytest-8.3.2, pluggy-1.6.0
rootdir: /Users/mario/Desktop/GECAD/Test4Py/docstring_parser
configfile: pyproject.toml
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_2_test_invalid_input_error_handling.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_________ ERROR at setup of test_compose_clean[source_expected_pairs0] _________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_2_test_invalid_input_error_handling.py, line 12
  def test_compose_clean(source_expected_pairs, expected):
E       fixture 'expected' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, source_expected_pairs, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_2_test_invalid_input_error_handling.py:12
_________ ERROR at setup of test_compose_clean[source_expected_pairs1] _________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_2_test_invalid_input_error_handling.py, line 12
  def test_compose_clean(source_expected_pairs, expected):
E       fixture 'expected' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, source_expected_pairs, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_2_test_invalid_input_error_handling.py:12
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_2_test_invalid_input_error_handling.py::test_compose_clean[source_expected_pairs0]
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_google_test_compose_clean_2_test_invalid_input_error_handling.py::test_compose_clean[source_expected_pairs1]
============================== 2 errors in 0.03s ===============================
"""