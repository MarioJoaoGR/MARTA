
import pytest
from docstring_parser.tests.test_numpydoc import parse  # Assuming this is the correct module path

@pytest.fixture
def source():
    return "Example numpy-style docstring with deprecation note."

@pytest.fixture
def expected_depr_version():
    return "1.0"

@pytest.fixture
def expected_depr_desc():
    return "This feature will be deprecated in version 1.0."

def test_deprecation(source, expected_depr_version, expected_depr_desc):
    """Test parsing deprecation notes from a given source string."""
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
collected 1 item

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_1_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_deprecation _______________________________

source = 'Example numpy-style docstring with deprecation note.'
expected_depr_version = '1.0'
expected_depr_desc = 'This feature will be deprecated in version 1.0.'

    def test_deprecation(source, expected_depr_version, expected_depr_desc):
        """Test parsing deprecation notes from a given source string."""
        docstring = parse(source)
    
>       assert docstring.deprecation is not None
E       assert None is not None
E        +  where None = <docstring_parser.common.Docstring object at 0x1060f6f80>.deprecation

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_1_test_invalid_input.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_1_test_invalid_input.py::test_deprecation
============================== 1 failed in 0.03s ===============================
"""