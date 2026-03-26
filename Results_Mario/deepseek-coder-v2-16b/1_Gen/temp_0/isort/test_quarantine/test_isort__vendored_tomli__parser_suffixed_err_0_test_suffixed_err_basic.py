
from isort._vendored.tomli._parser import TOMLDecodeError

def suffixed_err(src: str, pos: int, msg: str) -> TOMLDecodeError:
    """Return a `TOMLDecodeError` where error message is suffixed with coordinates in source."""
    
    def coord_repr(src: str, pos: int) -> str:
        if pos >= len(src):
            return "end of document"
        line = src.count("\n", 0, pos) + 1
        column = pos - src.rindex("\n", 0, pos) if line > 1 else pos + 1
        return f"line {line}, column {column}"
    
    coord_str = coord_repr(src, pos)
    error_msg = f"{msg} (at {coord_str})"
    return TOMLDecodeError(error_msg)

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
============================ no tests ran in 0.08s =============================
"""