
import pytest
from docstring_parser.numpydoc import Section, DocstringMeta
import inspect
import typing as T


def test_valid_input():
    section = Section(title="Parameters", key="params")
    section_text = "This is a description of the parameters."
    parsed_meta = list(section.parse(section_text))
    assert parsed_meta[0].args == ['params']
    assert parsed_meta[0].description == "This is a description of the parameters."