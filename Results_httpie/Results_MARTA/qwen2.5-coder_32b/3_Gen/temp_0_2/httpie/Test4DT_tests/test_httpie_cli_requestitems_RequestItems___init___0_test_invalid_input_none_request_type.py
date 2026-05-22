
import pytest
from unittest.mock import patch
from httpie.cli.requestitems import RequestItems, RequestType

def test_invalid_input_none_request_type():
    with patch('httpie.cli.requestitems.RequestType', new=lambda: None):
        request = RequestItems(request_type=None)
        assert request.is_json is True
