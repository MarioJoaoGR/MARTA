
def format_simplified(import_line: str) -> str:
    """
    Simplifies and formats an import line by removing the 'from' or 'import' keywords, if present.
    
    This function takes a string representing an import statement and returns a simplified version of that statement. 
    If the import line starts with "from ", it removes the "from" keyword and replaces "import" with dots (.). 
    If the import line starts with "import", it simply removes the "import" keyword.
    
    Parameters:
        import_line (str): A string representing an import statement, which may include 'from' or 'import'.
        
    Returns:
        str: The simplified and formatted import line, with 'from' and 'import' keywords removed if present.
    
    Examples:
        >>> format_simplified("from math import sqrt")
        "math.sqrt"
        
        >>> format_simplified("import os")
        "os"
        
        >>> format_simplified("   from   sys  import  argv   ")
        "sys.argv"
    """
    import_line = import_line.strip()
    if not (import_line.startswith("from ") or import_line.startswith("import ")):
        raise ValueError("Input string must start with 'from' or 'import'")
    
    if import_line.startswith("from "):
        import_line = import_line.replace("from ", "")
        import_line = import_line.replace(" import ", ".")
    elif import_line.startswith("import "):
        import_line = import_line.replace("import ", "")

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