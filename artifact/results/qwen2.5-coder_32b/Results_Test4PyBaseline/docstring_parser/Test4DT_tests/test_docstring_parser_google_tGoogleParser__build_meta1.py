
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS, DocstringMeta, SectionType

class TestGoogleParser:
    def test_build_meta_with_multiline_description(self):
        parser = GoogleParser()
        text = "param: This is a parameter\n    with a multiline description.\n    It should be handled correctly."
        meta = parser._build_meta(text, "Parameters")
        assert isinstance(meta, DocstringMeta)
        assert meta.description == "This is a parameter\nwith a multiline description.\nIt should be handled correctly."

    def test_build_meta_with_empty_lines_in_description(self):
        parser = GoogleParser()
        text = "param: This is a parameter\n\n    with an empty line in the middle."
        meta = parser._build_meta(text, "Parameters")
        assert isinstance(meta, DocstringMeta)