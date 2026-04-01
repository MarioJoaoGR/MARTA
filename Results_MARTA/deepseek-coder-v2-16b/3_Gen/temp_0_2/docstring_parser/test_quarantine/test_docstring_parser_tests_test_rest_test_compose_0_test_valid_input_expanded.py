
import pytest
from docstring_parser.tests.test_rest import RenderingStyle, parse, compose

@pytest.fixture(params=[RenderingStyle.COMPACT, RenderingStyle.EXPANDED])
def rendering_style(request):
    return request.param

def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
    """Test compose"""

    docstring = parse(
        """
        Short description.

        Long description.

        :param int foo: a description
        :param int bar: another description
        :return float: a return
        """
    )
    assert compose(docstring, rendering_style=rendering_style) == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
____________ ERROR at setup of test_compose[RenderingStyle.COMPACT] ____________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py, line 9
  def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
E       fixture 'expected' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, rendering_style, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py:9
___________ ERROR at setup of test_compose[RenderingStyle.EXPANDED] ____________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py, line 9
  def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
E       fixture 'expected' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, rendering_style, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py:9
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py::test_compose[RenderingStyle.COMPACT]
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py::test_compose[RenderingStyle.EXPANDED]
============================== 2 errors in 0.02s ===============================
"""