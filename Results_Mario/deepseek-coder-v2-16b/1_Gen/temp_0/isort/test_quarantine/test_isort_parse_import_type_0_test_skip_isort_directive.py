
# Importing config from isort.config
from isort.config import Config, DEFAULT_CONFIG

def import_type(line: str, config: Config = DEFAULT_CONFIG) -> str | None:
    """
    Determines whether a given line is an import statement and returns its type.
    
    This function checks if the line starts with 'import ', 'cimport ', or 'from ' to identify 
    if it's a straight import, from import, or no import at all. It also respects configuration 
    settings for ignoring certain lines based on 'noqa', 'isort:skip', and 'isort: split'.
    
    Parameters:
        line (str): The string representation of the line to be checked.
        config (Config, optional): An instance of Config class which contains configuration 
                                   settings for whether to honor 'noqa' directives and other import 
                                   sorting preferences. Defaults to DEFAULT_CONFIG.
    
    Returns:
        str | None: The type of the import statement if it is an import line ('straight' or 'from'), 
                     or None if the line should be ignored according to the configuration settings.
    
    Examples:
        >>> import_type("import os")
        'straight'
        
        >>> import_type("from math import sqrt")
        'from'
        
        >>> import_type(" # This is a comment, no import here")
        None
        
        >>> config = Config()
        >>> config.honor_noqa = False
        >>> import_type("# noqa: F401", config)
        'straight'  # Since honor_noqa is False, the line with "noqa" is not ignored.
    """
    if config.honor_noqa and line.lower().rstrip().endswith("noqa"):
        return None
    if "isort:skip" in line or "isort: skip" in line or "isort: split" in line:
        return None
    if line.startswith(("import ", "cimport ")):
        return "straight"
    if line.startswith("from "):
        return "from"
    return None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_parse_import_type_0_test_skip_isort_directive
isort/Test4DT_tests/test_isort_parse_import_type_0_test_skip_isort_directive.py:3:0: E0401: Unable to import 'isort.config' (import-error)
isort/Test4DT_tests/test_isort_parse_import_type_0_test_skip_isort_directive.py:3:0: E0611: No name 'config' in module 'isort' (no-name-in-module)


"""