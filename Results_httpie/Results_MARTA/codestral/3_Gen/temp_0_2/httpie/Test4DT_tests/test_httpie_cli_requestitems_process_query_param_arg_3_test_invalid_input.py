
import pytest
from httpie.cli.requestitems import KeyValueArg

def process_query_param_arg(arg: KeyValueArg) -> str:
    return arg.value

# Test case for invalid input
def test_invalid_input():
    with pytest.raises(AttributeError):
        # Attempt to pass an invalid argument type (e.g., a string instead of KeyValueArg)
        process_query_param_arg("invalid_argument")
