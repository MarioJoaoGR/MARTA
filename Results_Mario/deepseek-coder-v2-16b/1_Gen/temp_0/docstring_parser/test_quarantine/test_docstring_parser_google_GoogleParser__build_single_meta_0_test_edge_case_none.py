
import pytest
from docstring_parser import google
from docstring_parser.sections import Section, DEFAULT_SECTIONS

class GoogleParser:
    """Parser for Google-style docstrings."""
    def __init__(self, sections=None, title_colon=True):
        if not sections:
            sections = DEFAULT_SECTIONS
        self.sections = {s.title: s for s in sections}
        self.title_colon = title_colon
        self._setup()

    def _build_single_meta(self, section: Section, desc: str):
        if section.key in google.RETURNS_KEYWORDS | google.YIELDS_KEYWORDS:
            return google.DocstringReturns(
                args=[section.key],
                description=desc,
                type_name=None,
                is_generator=section.key in google.YIELDS_KEYWORDS,
            )
        if section.key in google.RAISES_KEYWORDS:
            return google.DocstringRaises(
                args=[section.key], description=desc, type_name=None
            )
        if section.key in google.EXAMPLES_KEYWORDS:
            return google.DocstringExample(
                args=[section.key], snippet=None, description=desc
            )
        if section.key in google.PARAM_KEYWORDS:
            raise ParseError("Expected parameter name.")
        return google.DocstringMeta(args=[section.key], description=desc)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_google_GoogleParser__build_single_meta_0_test_edge_case_none
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_0_test_edge_case_none.py:4:0: E0401: Unable to import 'docstring_parser.sections' (import-error)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_0_test_edge_case_none.py:4:0: E0611: No name 'sections' in module 'docstring_parser' (no-name-in-module)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_0_test_edge_case_none.py:13:8: E1101: Instance of 'GoogleParser' has no '_setup' member (no-member)
docstring_parser/Test4DT_tests/test_docstring_parser_google_GoogleParser__build_single_meta_0_test_edge_case_none.py:32:18: E0602: Undefined variable 'ParseError' (undefined-variable)

"""