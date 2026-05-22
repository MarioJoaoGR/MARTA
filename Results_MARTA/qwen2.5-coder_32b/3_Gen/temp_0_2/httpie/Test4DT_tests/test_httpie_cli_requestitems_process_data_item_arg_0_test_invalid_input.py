
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import KeyValueArg

def process_data_item_arg(arg: KeyValueArg) -> str:
    return arg.value

@pytest.mark.parametrize("invalid_input", [None, 123, {}])
def test_process_data_item_arg_invalid_input(invalid_input):
    with pytest.raises(AttributeError):
        process_data_item_arg(invalid_input)
