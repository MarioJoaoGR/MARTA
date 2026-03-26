
import ast
from typing import Optional, Dict, Tuple
import inspect
import textwrap
import pytest
from docstring_parser.attrdoc import AttributeDocstrings

class TestAttributeDocstrings:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.visitor = AttributeDocstrings()
    
    def test_none_input(self):
        # Test when the input is None
        with pytest.raises(TypeError):
            self.visitor.get_attr_docs(None)
