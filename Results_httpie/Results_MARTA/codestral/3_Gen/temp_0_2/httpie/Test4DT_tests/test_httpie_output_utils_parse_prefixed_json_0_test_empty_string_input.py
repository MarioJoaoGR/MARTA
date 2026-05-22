
import re
from typing import Tuple
from unittest.mock import patch

# Assuming PREFIX_REGEX is defined somewhere in the module or globally accessible
PREFIX_REGEX = r'__XSSI_PREFIX__'

def parse_prefixed_json(data: str) -> Tuple[str, str]:
    """Find the potential JSON body from `data`.

    Sometimes the JSON body is prefixed with a XSSI magic string, specific to the server. This function identifies and extracts this prefix from the input data and returns it along with the remaining part of the data that contains the actual JSON body.

    Parameters:
        data (str): The input string which may contain a JSON body prefixed by a special string.

    Returns:
        Tuple[str, str]: A tuple containing two elements:
            - `data_prefix` (str): The identified prefix of the JSON body.
            - `body` (str): The remaining part of the data after removing the prefix, which contains the actual JSON body.
    """
    matches = re.findall(PREFIX_REGEX, data)
    data_prefix = matches[0] if matches else ''
    body = data[len(data_prefix):]
    return data_prefix, body

def test_empty_string_input():
    with patch('httpie.output.utils.PREFIX_REGEX', new=r'__XSSI_PREFIX__'):
        data = ""
        prefix, body = parse_prefixed_json(data)
        assert prefix == ''
