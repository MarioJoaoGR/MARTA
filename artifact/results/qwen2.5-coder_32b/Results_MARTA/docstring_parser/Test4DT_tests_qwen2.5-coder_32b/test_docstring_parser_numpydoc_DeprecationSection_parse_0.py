
import pytest
from docstring_parser.numpydoc import DeprecationSection, DocstringDeprecated

def test_invalid_input_empty_string():
    deprecation_section = DeprecationSection(title="Deprecation", key="deprecation")
    text_empty = ""
    for deprecation in deprecation_section.parse(text_empty):
        assert deprecation.args == ['deprecation']
        assert deprecation.description is None
        assert deprecation.version is None

def test_valid_input_only_version():
    deprecation_section = DeprecationSection(title="Deprecation", key="deprecation")
    text_only_version = "1.3.0"
    for deprecation in deprecation_section.parse(text_only_version):
        assert deprecation.args == ['deprecation']
        assert deprecation.description is None
        assert deprecation.version == '1.3.0'

def test_valid_input_version_and_description():
    deprecation_section = DeprecationSection(title="Deprecation", key="deprecation")
    text_with_description = "1.2.0\nUse new_function instead."
    for deprecation in deprecation_section.parse(text_with_description):
        assert deprecation.args == ['deprecation']
        assert deprecation.description == 'Use new_function instead.'
        assert deprecation.version == '1.2.0'
