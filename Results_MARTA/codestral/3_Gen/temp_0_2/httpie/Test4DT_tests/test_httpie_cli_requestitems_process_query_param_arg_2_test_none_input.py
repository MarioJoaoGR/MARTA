
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import KeyValueArg

def process_query_param_arg(arg: KeyValueArg) -> str:
    return arg.value

def test_none_input():
    with pytest.raises(AttributeError):
        query_param = None
        result = process_query_param_arg(query_param)
