
import pytest
from docstring_parser.tests.test_numpydoc import parse

@pytest.fixture(scope="module")
def source():
    return """
    Some function to demonstrate deprecation.
    
    Deprecated since version 1.0.0: Use another_function instead.
    """

@pytest.mark.parametrize("source, expected_depr_version, expected_depr_desc", [
    ("""
    Some function to demonstrate deprecation.
    
    Deprecated since version 1.0.0: Use another_function instead.
    """, "1.0.0", "Use another_function instead."),
    ("""
    Some function to demonstrate no deprecation.
    """, None, None)
])
def test_deprecation(source, expected_depr_version, expected_depr_desc):
    docstring = parse(source)

    assert docstring.deprecation is not None
    assert docstring.deprecation.version == expected_depr_version
    assert docstring.deprecation.description == expected_depr_desc

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
_ test_deprecation[\n    Some function to demonstrate deprecation.\n    \n    Deprecated since version 1.0.0: Use another_function instead.\n    -1.0.0-Use another_function instead.] _

source = '\n    Some function to demonstrate deprecation.\n    \n    Deprecated since version 1.0.0: Use another_function instead.\n    '
expected_depr_version = '1.0.0'
expected_depr_desc = 'Use another_function instead.'

    @pytest.mark.parametrize("source, expected_depr_version, expected_depr_desc", [
        ("""
        Some function to demonstrate deprecation.
    
        Deprecated since version 1.0.0: Use another_function instead.
        """, "1.0.0", "Use another_function instead."),
        ("""
        Some function to demonstrate no deprecation.
        """, None, None)
    ])
    def test_deprecation(source, expected_depr_version, expected_depr_desc):
        docstring = parse(source)
    
>       assert docstring.deprecation is not None
E       assert None is not None
E        +  where None = <docstring_parser.common.Docstring object at 0x110791540>.deprecation

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py:26: AssertionError
_ test_deprecation[\n    Some function to demonstrate no deprecation.\n    -None-None] _

source = '\n    Some function to demonstrate no deprecation.\n    '
expected_depr_version = None, expected_depr_desc = None

    @pytest.mark.parametrize("source, expected_depr_version, expected_depr_desc", [
        ("""
        Some function to demonstrate deprecation.
    
        Deprecated since version 1.0.0: Use another_function instead.
        """, "1.0.0", "Use another_function instead."),
        ("""
        Some function to demonstrate no deprecation.
        """, None, None)
    ])
    def test_deprecation(source, expected_depr_version, expected_depr_desc):
        docstring = parse(source)
    
>       assert docstring.deprecation is not None
E       assert None is not None
E        +  where None = <docstring_parser.common.Docstring object at 0x110793490>.deprecation

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py:26: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py::test_deprecation[\n    Some function to demonstrate deprecation.\n    \n    Deprecated since version 1.0.0: Use another_function instead.\n    -1.0.0-Use another_function instead.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_missing_deprecation.py::test_deprecation[\n    Some function to demonstrate no deprecation.\n    -None-None]
============================== 2 failed in 0.03s ===============================
"""