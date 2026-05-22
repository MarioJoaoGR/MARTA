
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import KeyValueArg

def process_query_param_arg(arg: KeyValueArg) -> str:
    return arg.value

def test_edge_case_none():
    with patch('httpie.cli.requestitems.KeyValueArg', autospec=True):
        query_param = None
        with pytest.raises(AttributeError):
            process_query_param_arg(query_param)
