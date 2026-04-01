
import pytest
from docstring_parser.common import T

class DocstringExample:
    """DocstringMeta symbolizing example metadata.

    This class represents a documentation string example that can be used to provide metadata about code elements.

    Args:
        args (T.List[str]): A list of strings representing arguments required for the initialization.
        snippet (T.Optional[str]): An optional string containing a code snippet or part of it.
        description (T.Optional[str]): An optional string providing a brief description of the object.

    Examples:
        >>> example = DocstringExample(args=['arg1', 'arg2'], snippet='print("Hello, World!")', description='A simple example')
        >>> print(example.snippet)  # Outputs: print("Hello, World!")
        >>> print(example.description)  # Outputs: A simple example
    """
    def __init__(
        self,
        args: T.List[str],
        snippet: T.Optional[str],
        description: T.Optional[str],
    ) -> None:
        """Initialize self."""
        super().__init__()
        self.snippet = snippet
        self.description = description

def test_valid_inputs():
    example = DocstringExample(args=['arg1', 'arg2'], snippet='print("Hello, World!")', description='A simple example')
    
    assert example.snippet == 'print("Hello, World!")'
    assert example.description == 'A simple example'
