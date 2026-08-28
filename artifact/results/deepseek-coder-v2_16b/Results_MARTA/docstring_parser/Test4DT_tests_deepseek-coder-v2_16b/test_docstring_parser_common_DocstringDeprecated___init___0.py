
import pytest
from docstring_parser.common import DocstringDeprecated


def test_invalid_inputs():
    # Since __init__ does not expect a ValueError for invalid inputs, we should not raise one
    doc = DocstringDeprecated(args=["arg1"], description="This argument is no longer necessary.", version="1.0")
    assert isinstance(doc, DocstringDeprecated)