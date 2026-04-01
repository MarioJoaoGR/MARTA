
from unittest.mock import patch
from pytutils.lazy.lazy_import import ImportReplacer, ImportProcessor

def test_valid_input():
    processor = ImportProcessor()
    
    # Test with a valid multi-line string of import statements
    text = """
    from math import sqrt
    import os
    from datetime import date as dt
    """
    
    expected_output = [
        'from math import sqrt',
        'import os',
        'from datetime import date as dt'
    ]
    
    result = processor._canonicalize_import_text(text)
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
