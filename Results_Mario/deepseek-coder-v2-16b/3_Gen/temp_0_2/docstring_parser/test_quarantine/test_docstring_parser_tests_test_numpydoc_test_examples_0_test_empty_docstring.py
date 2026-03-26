
import pytest
from docstring_parser.tests.test_numpydoc import parse
import typing as T

@pytest.fixture(scope="module")
def source():
    return """
    A function that does something useful.
    Parameters:
        param1 (type): Description of param1.
        param2 (anotherType): Description of param2.
    Returns:
        returnValue (ReturnType): Description of return value.
    """

def test_examples(source, expected_results: T.List[T.Tuple[T.Optional[str], str]]):
    docstring = parse(source)
    assert len(docstring.meta) == len(expected_results)
    for meta, expected_result in zip(docstring.meta, expected_results):
        assert meta.description == expected_result[1]
    assert len(docstring.examples) == len(expected_results)
    for example, expected_result in zip(docstring.examples, expected_results):
        assert example.snippet == expected_result[0]
        assert example.description == expected_result[1]

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_empty_docstring.py E [100%]

==================================== ERRORS ====================================
_______________________ ERROR at setup of test_examples ________________________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_empty_docstring.py, line 17
  def test_examples(source, expected_results: T.List[T.Tuple[T.Optional[str], str]]):
E       fixture 'expected_results' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, source, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_empty_docstring.py:17
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_examples_0_test_empty_docstring.py::test_examples
=============================== 1 error in 0.03s ===============================
"""