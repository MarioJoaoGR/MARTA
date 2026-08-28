
import pytest
from docstring_parser.google import GoogleParser, Section

# Assuming DEFAULT_SECTIONS is defined somewhere in the module
# For the sake of this example, let's define a minimal set of default sections
DEFAULT_SECTIONS = [
    Section(title="Args", key="param", type="multiple"),
    Section(title="Returns", key="returns", type="singular")
]



def test_custom_sections_with_colons():
    custom_sections = [
        Section(title="Introduction", key="intro", type="singular"),
        Section(title="Conclusion", key="concl", type="singular")
    ]
    parser2 = GoogleParser(sections=custom_sections, title_colon=True)
    assert parser2.title_colon is True
    assert len(parser2.sections) == 2

def test_custom_sections_without_colons():
    custom_sections = [
        Section(title="Introduction", key="intro", type="singular"),
        Section(title="Conclusion", key="concl", type="singular")
    ]
    parser3 = GoogleParser(sections=custom_sections, title_colon=False)
    assert parser3.title_colon is False
    assert len(parser3.sections) == 2
