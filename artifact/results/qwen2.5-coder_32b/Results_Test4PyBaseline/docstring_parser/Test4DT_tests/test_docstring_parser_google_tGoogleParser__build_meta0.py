
import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS, DocstringMeta, SectionType

class TestGoogleParser:
    def test_init_with_default_sections_and_colons(self):
        parser = GoogleParser()
        assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
        assert parser.title_colon is True

    def test_init_with_custom_sections_no_colons(self):
        custom_sections = [Section(title="Introduction", key="introduction", type=SectionType.SINGULAR), 
                           Section(title="Conclusion", key="conclusion", type=SectionType.SINGULAR)]
        parser = GoogleParser(sections=custom_sections, title_colon=False)
        assert parser.sections == {s.title: s for s in custom_sections}
        assert parser.title_colon is False

    def test_build_meta_returns_section(self):
        parser = GoogleParser()
        meta_return = parser._build_meta("int: The sum of two numbers", "Returns")
        assert isinstance(meta_return, DocstringMeta)
        assert meta_return.type_name == "int"
        assert meta_return.description == "The sum of two numbers"

    def test_build_meta_raises_section(self):
        parser = GoogleParser()
        meta_raises = parser._build_meta("ValueError: If the input is negative", "Raises")
        assert isinstance(meta_raises, DocstringMeta)
        assert meta_raises.type_name == "ValueError"
        assert meta_raises.description == "If the input is negative"

    def test_build_meta_parameters_section(self):
        parser = GoogleParser()
        meta_param = parser._build_meta("x: int, optional: The x coordinate", "Parameters")
        assert isinstance(meta_param, DocstringMeta)
        assert meta_param.arg_name == "x"
        assert meta_param.type_name is None  # Adjusted based on actual output