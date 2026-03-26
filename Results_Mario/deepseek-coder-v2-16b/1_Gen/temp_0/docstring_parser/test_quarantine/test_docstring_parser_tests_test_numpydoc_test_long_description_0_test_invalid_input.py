
import pytest
from docstring_parser.tests.test_numpydoc import parse

@pytest.fixture(params=[
    ("A brief description of what this function does.\n\nExtended documentation or explanation follows here.", "A brief description of what this function does.", "Extended documentation or explanation follows here.", True),
    ("A brief description of what this function does.\n\nExtended documentation or explanation follows here.\n\nParameters:\n    param1 (type): Description of param1.\n    param2 (type): Description of param2.\n\nReturns:\n    type: Description of the return value.", "A brief description of what this function does.", "Extended documentation or explanation follows here.", True)
])
def source(request):
    return request.param[0]

def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
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
collected 2 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_invalid_input.py E [ 50%]
E                                                                        [100%]

==================================== ERRORS ====================================
_______________ ERROR at setup of test_long_description[source0] _______________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_invalid_input.py, line 12
  def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
E       fixture 'expected_short_desc' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, source, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_invalid_input.py:12
_______________ ERROR at setup of test_long_description[source1] _______________
file /Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_invalid_input.py, line 12
  def test_long_description(source, expected_short_desc, expected_long_desc, expected_blank):
E       fixture 'expected_short_desc' not found
>       available fixtures: anyio_backend, anyio_backend_name, anyio_backend_options, cache, capfd, capfdbinary, caplog, capsys, capsysbinary, doctest_namespace, free_tcp_port, free_tcp_port_factory, free_udp_port, free_udp_port_factory, include_metadata_in_junit_xml, json_metadata, metadata, monkeypatch, pytestconfig, record_property, record_testsuite_property, record_xml_attribute, recwarn, source, tmp_path, tmp_path_factory, tmpdir, tmpdir_factory
>       use 'pytest --fixtures [testpath]' for help on them.

/Users/mario/Desktop/GECAD/Test4Py/docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_invalid_input.py:12
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_invalid_input.py::test_long_description[source0]
ERROR docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_long_description_0_test_invalid_input.py::test_long_description[source1]
============================== 2 errors in 0.02s ===============================

"""