
import pytest
from docstring_parser.tests.test_numpydoc import parse

@pytest.mark.parametrize("source, expected_depr_version, expected_depr_desc", [
    ('', None, None),
    ('\n        A function that does something useful.\n        Deprecated since version 2.0.0: This feature is no longer supported and will be removed in future versions.\n    ', '2.0.0', 'This feature is no longer supported and will be removed in future versions.'),
    ('\n        A function that does something useful.\n        Deprecated since version 1.0.0: This feature is deprecated.\n    ', '1.0.0', 'This feature is deprecated.')
])
def test_deprecation(source, expected_depr_version, expected_depr_desc):
    docstring = parse(source)
    assert docstring.deprecation is not None
    if expected_depr_version:
        assert docstring.deprecation.version == expected_depr_version
    if expected_depr_desc:
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
collected 3 items

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_deprecation[-None-None] _________________________

source = '', expected_depr_version = None, expected_depr_desc = None

    @pytest.mark.parametrize("source, expected_depr_version, expected_depr_desc", [
        ('', None, None),
        ('\n        A function that does something useful.\n        Deprecated since version 2.0.0: This feature is no longer supported and will be removed in future versions.\n    ', '2.0.0', 'This feature is no longer supported and will be removed in future versions.'),
        ('\n        A function that does something useful.\n        Deprecated since version 1.0.0: This feature is deprecated.\n    ', '1.0.0', 'This feature is deprecated.')
    ])
    def test_deprecation(source, expected_depr_version, expected_depr_desc):
        docstring = parse(source)
>       assert docstring.deprecation is not None
E       assert None is not None
E        +  where None = <docstring_parser.common.Docstring object at 0x106026500>.deprecation

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input.py:12: AssertionError
_ test_deprecation[\n        A function that does something useful.\n        Deprecated since version 2.0.0: This feature is no longer supported and will be removed in future versions.\n    -2.0.0-This feature is no longer supported and will be removed in future versions.] _

source = '\n        A function that does something useful.\n        Deprecated since version 2.0.0: This feature is no longer supported and will be removed in future versions.\n    '
expected_depr_version = '2.0.0'
expected_depr_desc = 'This feature is no longer supported and will be removed in future versions.'

    @pytest.mark.parametrize("source, expected_depr_version, expected_depr_desc", [
        ('', None, None),
        ('\n        A function that does something useful.\n        Deprecated since version 2.0.0: This feature is no longer supported and will be removed in future versions.\n    ', '2.0.0', 'This feature is no longer supported and will be removed in future versions.'),
        ('\n        A function that does something useful.\n        Deprecated since version 1.0.0: This feature is deprecated.\n    ', '1.0.0', 'This feature is deprecated.')
    ])
    def test_deprecation(source, expected_depr_version, expected_depr_desc):
        docstring = parse(source)
>       assert docstring.deprecation is not None
E       assert None is not None
E        +  where None = <docstring_parser.common.Docstring object at 0x106027040>.deprecation

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input.py:12: AssertionError
_ test_deprecation[\n        A function that does something useful.\n        Deprecated since version 1.0.0: This feature is deprecated.\n    -1.0.0-This feature is deprecated.] _

source = '\n        A function that does something useful.\n        Deprecated since version 1.0.0: This feature is deprecated.\n    '
expected_depr_version = '1.0.0'
expected_depr_desc = 'This feature is deprecated.'

    @pytest.mark.parametrize("source, expected_depr_version, expected_depr_desc", [
        ('', None, None),
        ('\n        A function that does something useful.\n        Deprecated since version 2.0.0: This feature is no longer supported and will be removed in future versions.\n    ', '2.0.0', 'This feature is no longer supported and will be removed in future versions.'),
        ('\n        A function that does something useful.\n        Deprecated since version 1.0.0: This feature is deprecated.\n    ', '1.0.0', 'This feature is deprecated.')
    ])
    def test_deprecation(source, expected_depr_version, expected_depr_desc):
        docstring = parse(source)
>       assert docstring.deprecation is not None
E       assert None is not None
E        +  where None = <docstring_parser.common.Docstring object at 0x106024dc0>.deprecation

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input.py:12: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input.py::test_deprecation[-None-None]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input.py::test_deprecation[\n        A function that does something useful.\n        Deprecated since version 2.0.0: This feature is no longer supported and will be removed in future versions.\n    -2.0.0-This feature is no longer supported and will be removed in future versions.]
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_deprecation_0_test_invalid_input.py::test_deprecation[\n        A function that does something useful.\n        Deprecated since version 1.0.0: This feature is deprecated.\n    -1.0.0-This feature is deprecated.]
============================== 3 failed in 0.05s ===============================
"""