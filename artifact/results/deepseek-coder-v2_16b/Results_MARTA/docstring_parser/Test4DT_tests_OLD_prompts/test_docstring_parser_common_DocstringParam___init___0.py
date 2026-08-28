
import pytest
from docstring_parser.common import DocstringParam

def test_invalid_inputs():
    with pytest.raises(TypeError):
        # This should raise a TypeError because the constructor expects specific types for its arguments
        param = DocstringParam()
