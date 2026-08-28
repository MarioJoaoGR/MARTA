
import pytest
from docstring_parser.numpydoc import NumpydocParser, Section

# Assuming CustomSection1 and CustomSection2 are defined somewhere in your module
# For the sake of this example, let's define them here with minimal functionality.
class CustomSection1(Section):
    def __init__(self):
        super().__init__(title="Custom Section 1", title_pattern=r"Custom\s+Section\s+1")

class CustomSection2(Section):
    def __init__(self):
        super().__init__(title="Custom Section 2", title_pattern=r"Custom\s+Section\s+2")



def test_default_sections():
    parser = NumpydocParser()
    # Assuming DEFAULT_SECTIONS is a predefined set of sections in the module
    # Here we just check if there are any default sections loaded
    assert len(parser.sections) > 0

def test_parser_with_no_custom_sections():
    parser = NumpydocParser(sections=None)
    # Check if it falls back to default sections
    assert len(parser.sections) > 0