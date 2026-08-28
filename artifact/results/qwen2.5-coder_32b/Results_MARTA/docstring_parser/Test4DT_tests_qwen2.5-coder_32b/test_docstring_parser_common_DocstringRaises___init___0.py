
import pytest
from typing import List, Optional
from docstring_parser.common import DocstringMeta

# Base class definition (assuming)
class DocstringMeta:
    def __init__(self, args: List[str], description: Optional[str]):
        self.args = args
        self.description = description

# Derived class definition
class DocstringRaises(DocstringMeta):
    def __init__(
        self,
        args: List[str],
        description: Optional[str] = None,
        type_name: Optional[str] = None,
    ) -> None:
        super().__init__(args, description)
        self.type_name = type_name

# Test file
def test_DocstringRaises___init___basic():
    # Create an instance of DocstringRaises with basic parameters
    docstring_raises = DocstringRaises(
        args=['ValueError'],
        description='If the input is out of range',
        type_name='int'
    )
    
    # Assert that the attributes are set correctly
    assert docstring_raises.args == ['ValueError']
    assert docstring_raises.description == 'If the input is out of range'
    assert docstring_raises.type_name == 'int'
