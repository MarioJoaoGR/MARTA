
# Module: docstring_parser.common
# test_docstring.py
from your_module import Docstring, DocstringStyle, DocstringExample
import pytest

@pytest.fixture
def docstring_without_style():
    return Docstring()

@pytest.fixture
def docstring_with_custom_style():
    custom_style = DocstringStyle(format="custom", indent=4)
    return Docstring(style=custom_style)

@pytest.fixture
def docstring_with_examples():
    docstring_obj = Docstring()
    example1 = DocstringExample("This is the first example.", "example_tag_1")
    example2 = DocstringExample("Another example demonstrating usage.", "example_tag_2")
    docstring_obj.meta.extend([example1, example2])
    return docstring_obj

def test_init_without_style(docstring_without_style):
    assert docstring_without_style.short_description is None
    assert docstring_without_style.long_description is None
    assert not docstring_without_style.blank_after_short_description
    assert not docstring_without_style.blank_after_long_description
    assert docstring_without_style.meta == []
    assert docstring_without_style.style is None

def test_init_with_custom_style(docstring_with_custom_style):
    assert docstring_with_custom_style.short_description is None
    assert docstring_with_custom_style.long_description is None
    assert not docstring_with_custom_style.blank_after_short_description
    assert not docstring_with_custom_style.blank_after_long_description
    assert docstring_with_custom_style.meta == []
    assert isinstance(docstring_with_custom_style.style, DocstringStyle)

def test_examples_without_examples(docstring_without_style):
    assert docstring_without_style.examples() == []

def test_examples_with_examples(docstring_with_examples):
    examples = docstring_with_examples.examples()
    assert len(examples) == 2
    for example in examples:
        assert isinstance(example, DocstringExample)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_docstring_parser_common_Docstring_examples_0
docstring_parser/Test4DT_tests/test_docstring_parser_common_Docstring_examples_0.py:4:0: E0401: Unable to import 'your_module' (import-error)

"""