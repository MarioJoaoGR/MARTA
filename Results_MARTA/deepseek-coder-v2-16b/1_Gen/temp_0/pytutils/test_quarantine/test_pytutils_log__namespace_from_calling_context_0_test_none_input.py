
import inspect

def _namespace_from_calling_context(input_value=None):
    """
    Derive a namespace from the module containing the caller's caller.

    :param input_value: Optional input value to check for None (default is None).
    :type input_value: any
    :return: the fully qualified python name of a module.
    :rtype: str
    """
    if input_value is None:
        raise IndexError("Input cannot be None")
    return inspect.stack()[2][0].f_globals["__name__"]

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/pytutils
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.04s =============================
"""