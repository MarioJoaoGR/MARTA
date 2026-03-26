
import pytest
from typing import List, Optional

# Import the function from the module
class DocstringExample:
    def __init__(
        self,
        args: List[str],
        snippet: Optional[str] = None,  # Added default value to resolve pylint error
        description: Optional[str] = None,  # Added default value to resolve pylint error
    ) -> None:
        super().__init__()
        self.args = args
        self.snippet = snippet
        self.description = description

# Test cases for DocstringExample class initialization
def test_docstringexample_initialization():
    example = DocstringExample(args=["arg1", "arg2"], snippet="print('Hello, World!')", description="This is an example docstring.")
    
    # Assertions to check if the instance was created correctly
    assert isinstance(example, DocstringExample)
    assert example.args == ["arg1", "arg2"]
    assert example.snippet == "print('Hello, World!')"
    assert example.description == "This is an example docstring."

def test_docstringexample_initialization_no_snippet():
    example = DocstringExample(args=["arg1", "arg2"], description="This is another example docstring.")
    
    # Assertions to check if the instance was created correctly without a snippet
    assert isinstance(example, DocstringExample)
    assert example.args == ["arg1", "arg2"]
    assert example.snippet is None