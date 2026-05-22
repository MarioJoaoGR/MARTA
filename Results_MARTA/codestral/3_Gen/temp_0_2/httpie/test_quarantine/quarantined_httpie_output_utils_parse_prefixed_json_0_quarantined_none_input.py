
import re
from typing import Tuple
from unittest.mock import patch

def parse_prefixed_json(data: str) -> Tuple[str, str]:
    """Find the potential JSON body from `data`.

    Sometimes the JSON body is prefixed with a XSSI magic string, specific to the server.
    Return a tuple (data prefix, actual JSON body).

    """
    matches = re.findall(PREFIX_REGEX, data)
    data_prefix = matches[0] if matches else ''
    body = data[len(data_prefix):]
    return data_prefix, body

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_output_utils_parse_prefixed_json_0_test_none_input
httpie/Test4DT_tests_codestral/test_httpie_output_utils_parse_prefixed_json_0_test_none_input.py:13:25: E0602: Undefined variable 'PREFIX_REGEX' (undefined-variable)


"""