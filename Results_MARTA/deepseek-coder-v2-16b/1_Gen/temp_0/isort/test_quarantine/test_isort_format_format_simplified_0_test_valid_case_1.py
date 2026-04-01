
def format_simplified(import_line: str) -> str:
    import re
    
    # Remove leading and trailing whitespace
    import_line = import_line.strip()
    
    # Replace multiple spaces with a single space
    import_line = re.sub(' +', ' ', import_line)
    
    if import_line.startswith("from "):
        parts = import_line.split()
        if len(parts) > 1:
            return parts[1].replace('import', '.').rstrip('.')
    elif import_line.startswith("import "):
        parts = import_line.split()
        if len(parts) > 1:
            return parts[1].replace('import', '.')
    
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
============================ no tests ran in 0.05s =============================
"""