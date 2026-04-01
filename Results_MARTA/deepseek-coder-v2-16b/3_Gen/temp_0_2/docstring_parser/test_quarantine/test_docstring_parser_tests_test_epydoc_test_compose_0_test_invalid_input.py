
from docstring_parser.tests.test_epydoc import compose, parse

def test_compose(source: str, expected: str) -> None:
    """Test compose in default mode.

    This function tests the composition of a parsed docstring into its final formatted string representation using the `compose` function. It takes an input source string and an expected output string as parameters. The function parses the source string to extract metadata, then composes this metadata into a formatted string according to default settings. Finally, it asserts that the composed string matches the expected output string.

    Parameters:
        source (str): A string representing the input docstring in epydoc-style format. This string is parsed by the `parse` function before being passed to `compose`.
            - Changes to this parameter can affect how the docstring is parsed and ultimately rendered, so it should follow the conventions of an epydoc-style docstring for best results.
        expected (str): The expected output string after composing the parsed docstring. This serves as a reference for verifying that the `compose` function produces the correct result.
            - If the actual composed string does not match this expected output, the assertion will fail, indicating an issue with either the parsing or composition process.

    Returns:
        None: The function returns nothing but raises an AssertionError if the parsed and composed docstring do not match the expected output.

    Examples:
        To test the default mode of composing a docstring:
        ```python
        test_compose("Example source string", "Expected output string")
        ```

    Notes:
        - This function relies on the `parse` function to convert the input source string into a structured `Docstring` object.
        - The `compose` function is then used to format this parsed docstring according to default settings, which can be overridden by specifying different rendering styles or indentation levels in the call to `compose`.
        - Proper usage of this function requires that both the input source string and the expected output string accurately represent the intended metadata and formatting.
    """
    assert compose(parse(source)) == expected

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_invalid_input.py E [100%]

==================================== ERRORS ====================================
________________________ ERROR at setup of test_compose ________________________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_invalid_input.py, line 4
  def test_compose(source: str, expected: str) -> None:
E       fixture 'source' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_invalid_input.py:4
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_epydoc_test_compose_0_test_invalid_input.py::test_compose
=============================== 1 error in 0.03s ===============================
"""