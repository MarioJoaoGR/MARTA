
import pytest
from docstring_parser.common import DocstringReturns

def test_valid_non_generator():
    # Test initializing a non-generator function returning an integer
    doc_return = DocstringReturns(
        args=[],
        description="The sum of two numbers",
        type_name="int",
        is_generator=False,
    )
    assert doc_return.type_name == "int"
    assert doc_return.is_generator is False

def test_valid_generator():
    # Test initializing a generator yielding strings
    doc_yield = DocstringReturns(
        args=["index"],
        description="Yields the next string in sequence",
        type_name="str",
        is_generator=True,
        return_name="next_string"
    )
    assert doc_yield.type_name == "str"
    assert doc_yield.is_generator is True

def test_valid_no_description():
    # Test initializing a function returning None with no description
    doc_none_return = DocstringReturns(
        args=[],
        description=None,
        type_name="None",
        is_generator=False,
    )
    assert doc_none_return.description is None
    assert doc_none_return.type_name == "None"

def test_invalid_missing_args():
    # Test initializing with missing required argument 'args'
    with pytest.raises(TypeError):
        DocstringReturns(
            description="The sum of two numbers",
            type_name="int",
            is_generator=False,
        )

def test_invalid_missing_description():
    # Test initializing with missing required argument 'description'
    with pytest.raises(TypeError):
        DocstringReturns(
            args=[],
            type_name="int",
            is_generator=False,
        )

def test_invalid_missing_type_name():
    # Test initializing with missing required argument 'type_name'
    with pytest.raises(TypeError):
        DocstringReturns(
            args=[],
            description="The sum of two numbers",
            is_generator=False,
        )

def test_invalid_missing_is_generator():
    # Test initializing with missing required argument 'is_generator'
    with pytest.raises(TypeError):
        DocstringReturns(
            args=[],
            description="The sum of two numbers",
            type_name="int",
        )
