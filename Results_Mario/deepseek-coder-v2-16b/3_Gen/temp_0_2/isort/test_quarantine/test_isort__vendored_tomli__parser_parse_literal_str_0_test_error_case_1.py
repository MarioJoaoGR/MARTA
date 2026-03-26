
from typing import Tuple

def parse_literal_str(src: str, pos: int) -> Tuple[int, str]:
    """Parses a literal string from the source code `src` starting at position `pos`. The function skips past the initial apostrophe and then collects characters until it encounters another apostrophe. It returns the updated position after the ending apostrophe and the parsed string without the surrounding apostrophes.
    
    Parameters:
        src (str): The input string or text from which to parse the literal string.
        pos (int): The current position in the source string where parsing should start or continue. This parameter is updated to reflect the new position after skipping past the initial apostrophe.
    
    Returns:
        Tuple[int, str]: A tuple containing the updated position after the ending apostrophe and the parsed literal string without the surrounding apostrophes.
    
    Example:
        ```python
        src = "''hello world'"
        pos = 0
        new_pos, lit_str = parse_literal_str(src, pos)
        print(new_pos)  # Outputs: 12
        print(lit_str)  # Outputs: hello world
        
        src = "''hello' 'world'"
        pos = 0
        new_pos, lit_str = parse_literal_str(src, pos)
        print(new_pos)  # Outputs: 8
        print(lit_str)  # Outputs: hello
        
        src = "''hello' 'world'"
        pos = 0
        new_pos, lit_str = parse_literal_str(src, pos)
        print(new_pos)  # Outputs: 8
        print(lit_str)  # Outputs: hello
        ```
        
    In the first example, `parse_literal_str` skips past the initial apostrophe and collects characters until it encounters another apostrophe, returning the updated position and the parsed string "hello world". The second example demonstrates that if there is an additional space within the literal string, it will be included in the returned string.
    """
    pos += 1  # Skip starting apostrophe
    start_pos = pos
    while pos < len(src) and src[pos] != "'":
        pos += 1
    return pos + 1, src[start_pos:pos]  # Return the parsed string without surrounding apostrophes

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