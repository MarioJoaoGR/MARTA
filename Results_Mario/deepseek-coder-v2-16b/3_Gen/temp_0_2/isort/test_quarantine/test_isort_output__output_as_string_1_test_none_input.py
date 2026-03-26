
def _output_as_string(lines: list[str], line_separator: str) -> str:
    """
    Combines a list of strings into a single string with normalized empty lines, using the specified line separator.
    
    Parameters:
        lines (list[str]): A list of strings where each element represents a line from the text.
        line_separator (str): The string to use as a separator between lines in the final output.
        
    Returns:
        str: A single string that concatenates all elements of the input list, with normalized empty lines and the specified line separator used between each pair of adjacent lines.
        
    Examples:
        >>> _output_as_string(["Hello, world!", "", "   ", ""], "\n")
        'Hello, world!\n\n   \n'
        
        >>> _output_as_string(["Line one.", "Line two."], " | ")
        'Line one. | Line two.'
    """
    if lines is None:
        return ""
    return line_separator.join(_normalize_empty_lines(lines))

def _normalize_empty_lines(lines: list[str]) -> list[str]:
    while lines and lines[-1].strip() == "":
        lines.pop(-1)
    if not lines:
        return [""]  # Ensure at least one empty line if the list is empty
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
============================ no tests ran in 0.06s =============================
"""