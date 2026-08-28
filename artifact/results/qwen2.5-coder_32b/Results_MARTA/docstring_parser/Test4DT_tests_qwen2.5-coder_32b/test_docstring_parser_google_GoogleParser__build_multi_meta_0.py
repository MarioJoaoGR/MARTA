
import pytest
from docstring_parser.google import GoogleParser, Section, DocstringParam, DocstringReturns, DocstringRaises


def test_build_multi_meta_returns():
    parser = GoogleParser()
    section_returns = Section(title="Returns", key="returns", type="return")
    meta_return = parser._build_multi_meta(
        section=section_returns,
        before="int",
        desc="The sum of two numbers."
    )
    assert isinstance(meta_return, DocstringReturns)
    assert meta_return.type_name == "int"
    assert meta_return.description == "The sum of two numbers."

def test_build_multi_meta_raises():
    parser = GoogleParser()
    section_raises = Section(title="Raises", key="raises", type="exception")
    meta_raise = parser._build_multi_meta(
        section=section_raises,
        before="ValueError",
        desc="If the input is out of range."
    )
    assert isinstance(meta_raise, DocstringRaises)
    assert meta_raise.type_name == "ValueError"
    assert meta_raise.description == "If the input is out of range."

def test_build_multi_meta_no_type():
    parser = GoogleParser()
    section_params = Section(title="Args", key="param", type="parameter")
    meta_param = parser._build_multi_meta(
        section=section_params,
        before="item_count",
        desc="The number of items to process."
    )
    assert isinstance(meta_param, DocstringParam)
    assert meta_param.arg_name == "item_count"
    assert meta_param.type_name is None
