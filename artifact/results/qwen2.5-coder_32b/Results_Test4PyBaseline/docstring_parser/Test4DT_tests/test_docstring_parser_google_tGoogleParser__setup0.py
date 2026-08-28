
# Test case  
# Module: docstring_parser.google
import pytest
from docstring_parser.google import GoogleParser
from typing import List, Optional

# Mocking the Section class as it's not provided in the given code snippet
class Section:
    def __init__(self, title: str):
        self.title = title


# Assuming DEFAULT_SECTIONS is defined somewhere in the module or we can define a mock version for testing
DEFAULT_SECTIONS = [
    Section(title="Args"),
    Section(title="Returns"),
    Section(title="Examples")
]


def test_google_parser_default_sections_with_colons():
    parser = GoogleParser()
    expected_sections = {s.title: s for s in parser.sections.values()}
    assert parser.sections == expected_sections
    assert parser.title_colon is True


def test_google_parser_custom_sections_without_colons():
    custom_sections = [Section(title="Introduction"), Section(title="Conclusion")]
    parser = GoogleParser(sections=custom_sections, title_colon=False)
    assert parser.sections == {s.title: s for s in custom_sections}
    assert parser.title_colon is False


def test_google_parser_default_sections_without_colons():
    parser = GoogleParser(title_colon=False)
    expected_sections = {s.title: s for s in parser.sections.values()}
    assert parser.sections == expected_sections
    assert parser.title_colon is False


def test_google_parser_custom_sections_with_colons():
    custom_sections = [Section(title="Setup"), Section(title="Usage")]
    parser = GoogleParser(sections=custom_sections, title_colon=True)
    assert parser.sections == {s.title: s for s in custom_sections}
    assert parser.title_colon is True


def test_google_parser_no_sections_provided():
    parser = GoogleParser(None, title_colon=True)
    expected_sections = {s.title: s for s in parser.sections.values()}
    assert parser.sections == expected_sections
    assert parser.title_colon is True
