
# Define the mapping outside the function to avoid undefined variable errors
_STR_BOOLEAN_MAPPING = {
    'true': True,
    't': True,
    'yes': True,
    'y': True,
    'on': True,
    '1': True,
    'false': False,
    'f': False,
    'no': False,
    'n': False,
    'off': False,
    '0': False
}

def _as_bool(value: str) -> bool:
    """Given a string value that represents True or False, returns the Boolean equivalent.
    Heavily inspired from distutils strtobool.
    """
    try:
        return _STR_BOOLEAN_MAPPING[value.lower()]
    except KeyError:
        raise ValueError(f"invalid truth value {value}")

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.05s =============================
"""