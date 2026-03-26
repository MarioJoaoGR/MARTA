
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringReturns

def test_edge_cases():
    # Test initialization with all parameters provided
    metadata = DocstringReturns(args=["arg1", "arg2"], description="This function does something.", type_name="int", is_generator=False, return_name="result")
    assert isinstance(metadata.type_name, str)
    assert metadata.type_name == "int"
    assert isinstance(metadata.is_generator, bool)
    assert not metadata.is_generator
    assert isinstance(metadata.return_name, str)
    assert metadata.return_name == "result"

    # Test initialization with some parameters omitted
    metadata_no_return = DocstringReturns(args=["arg1", "arg2"], description="This function does something.", type_name="int", is_generator=False)
    assert isinstance(metadata_no_return.type_name, str)
    assert metadata_no_return.type_name == "int"
    assert isinstance(metadata_no_return.is_generator, bool)
    assert not metadata_no_return.is_generator
    assert metadata_no_return.return_name is None
