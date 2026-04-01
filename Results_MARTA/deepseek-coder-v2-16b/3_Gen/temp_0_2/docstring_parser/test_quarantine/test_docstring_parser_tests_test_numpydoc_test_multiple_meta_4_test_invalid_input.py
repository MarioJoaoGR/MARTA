
import pytest
from docstring_parser.tests.test_numpydoc import parse

def test_multiple_meta() -> None:
    """Test parsing multiple meta."""
    with pytest.raises(AssertionError):
        docstring = parse(
            """
            Short description

            Parameters
            ----------
            spam
                asd
                1
                    2
                3

            Raises
            ------
            bla
                herp
            yay
                derp
            """
        )
        assert docstring.short_description == "Short description"
        assert len(docstring.meta) == 3
        assert docstring.meta[0].args == ["param", "spam"]
        assert docstring.meta[0].arg_name == "spam"
        assert docstring.meta[0].description == "asd\n1\n    2\n3"
        assert docstring.meta[1].args == ["raises", "bla"]
        assert docstring.meta[1].type_name == "bla"
        assert docstring.meta[1].description == "herp"
        assert docstring.meta[2].args == ["raises", "yay"]
        assert docstring.meta[2].type_name == "yay"
        assert docstring.meta[2].description == "derp"

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

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_multiple_meta_4_test_invalid_input.py F [100%]

=================================== FAILURES ===================================
______________________________ test_multiple_meta ______________________________

    def test_multiple_meta() -> None:
        """Test parsing multiple meta."""
>       with pytest.raises(AssertionError):
E       Failed: DID NOT RAISE <class 'AssertionError'>

docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_multiple_meta_4_test_invalid_input.py:7: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED docstring_parser/Test4DT_tests/test_docstring_parser_tests_test_numpydoc_test_multiple_meta_4_test_invalid_input.py::test_multiple_meta
============================== 1 failed in 0.04s ===============================
"""