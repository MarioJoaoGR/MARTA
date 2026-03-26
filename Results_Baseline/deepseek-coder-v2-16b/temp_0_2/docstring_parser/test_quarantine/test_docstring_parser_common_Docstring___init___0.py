
# Module: docstring_parser.common
# test_docstring.py
from docstring_parser.common import Docstring, DocstringStyle
import pytest

@pytest.fixture
def default_docstring():
    return Docstring()

@pytest.fixture
def custom_style_docstring():
    style = DocstringStyle(format="custom", indent=4)
    return Docstring(style=style)

# Test initialization with default parameters
def test_init_default(default_docstring):
    assert default_docstring.short_description is None
    assert default_docstring.long_description is None
    assert not default_docstring.blank_after_short_description
    assert not default_docstring.blank_after_long_description
    assert len(default_docstring.meta) == 0
    assert default_docstring.style is None

# Test initialization with custom style
def test_init_custom_style(custom_style_docstring):
    assert isinstance(custom_style_docstring.style, DocstringStyle)
    assert custom_style_docstring.style.format == "custom"
    assert custom_style_docstring.style.indent == 4

# Test adding a valid argument
def test_add_valid_argument(default_docstring):
    default_docstring.add_argument({'name': 'param1', 'type': 'int', 'description': 'The first parameter.'})
    assert len(default_docstring.meta) == 1
    assert default_docstring.meta[0].name == 'param1'
    assert default_docstring.meta[0].type == 'int'
    assert default_docstring.meta[0].description == 'The first parameter.'

# Test adding an invalid argument (missing keys)
def test_add_invalid_argument(default_docstring):
    with pytest.raises(ValueError):
        default_docstring.add_argument({'name': 'param1', 'type': 'int'})
    assert len(default_docstring.meta) == 0

# Test retrieving arguments
def test_get_arguments(default_docstring):
    default_docstring.add_argument({'name': 'param1', 'type': 'int', 'description': 'The first parameter.'})
    args = default_docstring.get_arguments()
    assert len(args) == 1
    assert args[0]['name'] == 'param1'
    assert args[0]['type'] == 'int'
    assert args[0]['description'] == 'The first parameter.'

# Test converting to dictionary
def test_to_dict(default_docstring):
    default_docstring.add_argument({'name': 'param1', 'type': 'int', 'description': 'The first parameter.'})
    expected_dict = {
        'short_description': None,
        'long_description': None,
        'blank_after_short_description': False,
        'blank_after_long_description': False,
        'meta': [],
        'style': None
    }
    assert default_docstring.to_dict() == expected_dict

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_Docstring___init___0
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring___init___0.py:13:12: E1123: Unexpected keyword argument 'format' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring___init___0.py:13:12: E1123: Unexpected keyword argument 'indent' in constructor call (unexpected-keyword-arg)
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring___init___0.py:13:12: E1120: No value for argument 'value' in constructor call (no-value-for-parameter)

"""