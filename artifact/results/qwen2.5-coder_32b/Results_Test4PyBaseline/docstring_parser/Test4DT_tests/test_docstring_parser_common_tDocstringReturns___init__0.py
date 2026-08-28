# Module: docstring_parser.common
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringReturns

class DocstringMeta:
    def __init__(self, args: List[str], description: Optional[str]):
        self.args = args
        self.description = description


def test_docstring_returns_non_generator_with_all_params():
    doc_return = DocstringReturns(
        args=["return"],
        description="The sum of two numbers",
        type_name="int",
        is_generator=False,
        return_name="result"
    )
    assert doc_return.args == ["return"]
    assert doc_return.description == "The sum of two numbers"
    assert doc_return.type_name == "int"
    assert not doc_return.is_generator
    assert doc_return.return_name == "result"


def test_docstring_returns_generator_without_optional_param():
    gen_doc_return = DocstringReturns(
        args=[],
        description="Yields the next number in the sequence",
        type_name="int",
        is_generator=True
    )
    assert gen_doc_return.args == []
    assert gen_doc_return.description == "Yields the next number in the sequence"
    assert gen_doc_return.type_name == "int"
    assert gen_doc_return.is_generator
    assert gen_doc_return.return_name is None


def test_docstring_returns_minimal_required_params():
    minimal_doc_return = DocstringReturns(
        args=[],
        description="The processed data",
        type_name="List[str]",
        is_generator=False
    )
    assert minimal_doc_return.args == []
    assert minimal_doc_return.description == "The processed data"
    assert minimal_doc_return.type_name == "List[str]"
    assert not minimal_doc_return.is_generator
    assert minimal_doc_return.return_name is None


def test_docstring_returns_non_generator_with_no_type():
    no_type_doc_return = DocstringReturns(
        args=["return"],
        description="A dictionary containing user information",
        type_name=None,
        is_generator=False,
        return_name="user_info"
    )
    assert no_type_doc_return.args == ["return"]
    assert no_type_doc_return.description == "A dictionary containing user information"
    assert no_type_doc_return.type_name is None
    assert not no_type_doc_return.is_generator
    assert no_type_doc_return.return_name == "user_info"


def test_docstring_returns_with_empty_description():
    empty_desc_doc_return = DocstringReturns(
        args=["return"],
        description="",
        type_name="str",
        is_generator=False,
        return_name="empty"
    )
    assert empty_desc_doc_return.args == ["return"]
    assert empty_desc_doc_return.description == ""
    assert empty_desc_doc_return.type_name == "str"
    assert not empty_desc_doc_return.is_generator
    assert empty_desc_doc_return.return_name == "empty"


def test_docstring_returns_with_empty_args():
    empty_args_doc_return = DocstringReturns(
        args=[],
        description="A list of items",
        type_name="List[Item]",
        is_generator=False,
        return_name="items"
    )
    assert empty_args_doc_return.args == []
    assert empty_args_doc_return.description == "A list of items"
    assert empty_args_doc_return.type_name == "List[Item]"
    assert not empty_args_doc_return.is_generator
    assert empty_args_doc_return.return_name == "items"


def test_docstring_returns_with_none_description():
    none_desc_doc_return = DocstringReturns(
        args=["return"],
        description=None,
        type_name="Dict[str, int]",
        is_generator=False,
        return_name="counts"
    )
    assert none_desc_doc_return.args == ["return"]
    assert none_desc_doc_return.description is None
    assert none_desc_doc_return.type_name == "Dict[str, int]"
    assert not none_desc_doc_return.is_generator
    assert none_desc_doc_return.return_name == "counts"
