
def _normalize_empty_lines(lines: list[str]) -> list[str]:
    """
    Normalizes the spacing of empty lines at the end of a list of strings.
    
    This function removes trailing empty lines and ensures there is exactly one empty line at the end of the list.
    
    Parameters:
        lines (list[str]): A list of string where each element represents a line from the text.
        
    Returns:
        list[str]: The modified list with normalized spacing for empty lines.
        
    Examples:
        >>> _normalize_empty_lines(["", ""])
        ['', '', '']
        
        >>> _normalize_empty_lines(["line1", "", "", "line2"])
        ['line1', '', '', '']
        
        >>> _normalize_empty_lines([])
        ['']
    """
    while lines and lines[-1].strip() == "":
        lines.pop(-1)

    if not lines:
        lines.append("")
    elif lines[-1] != "":
        lines.append("")
    
    return lines

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
============================ no tests ran in 0.07s =============================
"""