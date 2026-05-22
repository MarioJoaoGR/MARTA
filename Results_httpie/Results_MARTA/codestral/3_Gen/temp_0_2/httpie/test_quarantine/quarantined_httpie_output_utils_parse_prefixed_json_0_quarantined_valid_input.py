
import re
from typing import Tuple
from unittest.mock import patch

def parse_prefixed_json(data: str) -> Tuple[str, str]:
    """Find the potential JSON body from `data`.

    Sometimes the JSON body is prefixed with a XSSI magic string, specific to the server. This function identifies and extracts this prefix from the input data and returns it along with the remaining part of the data that contains the actual JSON body.

    Parameters:
        data (str): The input string which may contain a JSON body prefixed by a special string.

    Returns:
        Tuple[str, str]: A tuple containing two elements:
            - `data_prefix` (str): The identified prefix of the JSON body.
            - `body` (str): The remaining part of the data after removing the prefix, which contains the actual JSON body.

    Example:
        >>> parse_prefixed_json('__XSSI_PREFIX__ {"key": "value"}')
        ('__XSSI_PREFIX__', '{"key": "value"}')

        In this example, '__XSSI_PREFIX__' is identified as the prefix and removed from the data to leave the JSON body.
    """
    matches = re.findall(r'__XSSI_PREFIX__', data)
    data_prefix = matches[0] if matches else ''
    body = data[len(data_prefix):]
    return data_prefix, body

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
============================ no tests ran in 0.04s =============================
"""