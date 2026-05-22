
import argparse
from httpie.client import HTTPHeadersDict

# Assuming DEFAULT_UA, JSON_ACCEPT, JSON_CONTENT_TYPE, FORM_CONTENT_TYPE are defined elsewhere in your codebase or standard library
DEFAULT_UA = "httpie/1.0"
JSON_ACCEPT = "application/json"
JSON_CONTENT_TYPE = "application/json"
FORM_CONTENT_TYPE = "application/x-www-form-urlencoded"

def make_default_headers(args: argparse.Namespace) -> HTTPHeadersDict:
    default_headers = HTTPHeadersDict({
        'User-Agent': DEFAULT_UA
    })

    auto_json = args.data and not args.form
    if args.json or auto_json:
        default_headers['Accept'] = JSON_ACCEPT
        if (args.json or (auto_json and args.data)):
            default_headers['Content-Type'] = JSON_CONTENT_TYPE
    elif args.form and not args.files:
        # If sending files, `requests` will set
        # the `Content-Type` for us.
        default_headers['Content-Type'] = FORM_CONTENT_TYPE
    return default_headers

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
============================ no tests ran in 0.22s =============================
"""