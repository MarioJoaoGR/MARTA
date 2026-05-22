
from unittest.mock import patch, Mock
import httpie.cli.nested_json.interpret

def unwrap_top_level_list_if_needed(data: dict):
    """
    Propagate the top-level list, if that’s what we got.
    """
    if len(data) == 1:
        key, value = list(data.items())[0]
        if isinstance(value, httpie.cli.nested_json.interpret.NestedJSONArray):
            assert key == ""
            return value
    return data

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
============================ no tests ran in 0.09s =============================
"""