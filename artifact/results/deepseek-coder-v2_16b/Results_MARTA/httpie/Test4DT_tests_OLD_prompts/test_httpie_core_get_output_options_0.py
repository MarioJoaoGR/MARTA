
import pytest
from unittest.mock import patch
import requests
import argparse
from httpie.core import get_output_options, OUT_REQ_HEAD, OUT_REQ_BODY, OUT_RESP_HEAD, OUT_RESP_BODY

def test_invalid_input_error_handling():
    with pytest.raises(AttributeError):
        args = 'invalid_arg'
        req = requests.PreparedRequest()
        result = get_output_options(args, req)
