
def format_natural(import_line: str) -> str:
    """
    Formats an import line string to a more natural Python import statement.
    
    This function takes an import line as input and formats it into either a simple 'import' or a 'from ... import ...' statement, depending on the content of the input string.
    
    Parameters:
        import_line (str): The import line to be formatted. It should be a string representing either a module name or an import statement with dots.
        
        Example usage:
            >>> format_natural("math")
            'import math'
            
            >>> format_natural("from math import sin")
            'from math import sin'
            
            >>> format_natural("math.sin")
            'from math import sin'
    
    Returns:
        str: The formatted import statement or the original input if it does not match the expected patterns.
        
        Example output:
            >>> format_natural("math")
            'import math'
            
            >>> format_natural("math.sin")
            'from math import sin'
    """
    if import_line is None:
        return 'import None'
    
    import_line = import_line.strip()
    if not import_line.startswith("from ") and not import_line.startswith("import "):
        if "." not in import_line:
            return f"import {import_line}"
        parts = import_line.split(".")
        end = parts.pop(-1)
        return f"from {'.'.join(parts)} import {end}"

    return import_line

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