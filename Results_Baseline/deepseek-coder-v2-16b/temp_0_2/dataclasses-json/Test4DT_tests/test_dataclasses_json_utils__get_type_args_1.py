
import pytest
from typing import Tuple, Union
from dataclasses_json.utils import _NO_ARGS, _get_type_args

# Test cases for _get_type_args function
def test_get_type_args_with_generic_type():
    """Test that it retrieves the type arguments correctly."""
    from typing import Tuple
    tp = Tuple[int, str]
    result = _get_type_args(tp)
    assert result == (int, str)

def test_get_type_args_without_default():
    """Test that it returns the default value when no specific default is provided."""
    from typing import Tuple
    tp = Tuple[int, str]
    result = _get_type_args(tp)