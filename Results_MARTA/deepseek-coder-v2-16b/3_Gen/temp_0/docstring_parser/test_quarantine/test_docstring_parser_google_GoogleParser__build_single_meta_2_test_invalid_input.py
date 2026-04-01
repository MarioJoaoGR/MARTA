
import pytest
from googleparser import GoogleParser, Section
from docstring_parser.google import DEFAULT_SECTIONS, ParseError
from docstring_parser.common import DocstringMeta, DocstringReturns, DocstringRaises, DocstringExample

RETURNS_KEYWORDS = {"return"}
YIELDS_KEYWORDS = {"yield"}
RAISES_KEYWORDS = {"raise"}
EXAMPLES_KEYWORDS = {"example"}
PARAM_KEYWORDS = {"param"}

def test_invalid_input():
    with pytest.raises(ParseError):
        # Provide an unsupported section key
        invalid_section = Section("Unsupported", "This is an unsupported section.")
        parser = GoogleParser([invalid_section], title_colon=True)
        
        # The following line should raise a ParseError due to the unsupported section key
        assert parser._build_single_meta(invalid_section, "This is the description.")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_GoogleParser__build_single_meta_2_test_invalid_input
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_2_test_invalid_input.py:3:0: E0401: Unable to import 'googleparser' (import-error)


"""