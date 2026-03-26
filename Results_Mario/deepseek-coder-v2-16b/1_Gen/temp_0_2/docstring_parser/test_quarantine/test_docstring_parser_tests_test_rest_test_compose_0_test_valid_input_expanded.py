
import pytest
from docstring_parser.tests.test_rest import RenderingStyle, parse, compose

@pytest.fixture(params=[RenderingStyle.COMPACT, RenderingStyle.CLEAN, RenderingStyle.EXPANDED])
def rendering_style(request):
    return request.param

def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
    """Test compose function by parsing a ReST-style docstring and ensuring it matches the expected output when rendered with the given rendering style.

    This function takes a `rendering_style` which determines how the parsed docstring should be formatted, and an `expected` string that represents the desired outcome of the composition process. It parses a sample ReST-style docstring using the `parse` function, then composes it with the specified rendering style and compares the result to the expected output.

    Parameters:
        rendering_style (RenderingStyle): The style in which to render the parsed docstring. Must be one of RenderingStyle.COMPACT, RenderingStyle.CLEAN, or RenderingStyle.EXPANDED.
        expected (str): A string representing the expected output format for the composed docstring.

    Returns:
        None: This function does not return any value but raises an assertion error if the composition result does not match the expected output.

    Examples:
        >>> test_compose(RenderingStyle.COMPACT, "Expected compact style output.")
        >>> test_compose(RenderingStyle.CLEAN, "Expected clean style output.")
        >>> test_compose(RenderingStyle.EXPANDED, "Expected expanded style output.")
        
    Note:
        The `rendering_style` parameter should be an instance of the RenderingStyle enum, specifying one of the three possible rendering styles for the docstring composition. The expected string should accurately represent the desired formatted output to ensure proper testing and validation of the compose function's behavior.
    
    Test compose function.

    This function tests the composition of a docstring based on the specified rendering style and compares it to an expected output string. It parses a sample docstring with parameter and return descriptions and uses them to generate a formatted string according to the given RenderingStyle. The test then asserts that the generated string matches the expected output.

    Parameters:
        rendering_style (RenderingStyle): The style in which the docstring should be rendered.
        expected (str): The expected output string after composing the parsed docstring.

    Returns:
        None
    """
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
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py E [ 33%]
EE                                                                       [100%]

==================================== ERRORS ====================================
____________ ERROR at setup of test_compose[RenderingStyle.COMPACT] ____________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py, line 9
  def test_compose(rendering_style: RenderingStyle, expected: str) -> None:
E       fixture 'expected' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, rendering_style, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py:9
_____________ ERROR at setup of test_compose[RenderingStyle.CLEAN] _____________
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
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py::test_compose[RenderingStyle.CLEAN]
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_rest_test_compose_0_test_valid_input_expanded.py::test_compose[RenderingStyle.EXPANDED]
============================== 3 errors in 0.02s ===============================
"""