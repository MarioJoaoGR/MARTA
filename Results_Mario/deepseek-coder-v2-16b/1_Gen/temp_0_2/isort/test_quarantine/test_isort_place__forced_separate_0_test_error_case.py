
import fnmatch
from isort.place import Config  # Assuming this import path is correct based on your project structure

def _forced_separate(name: str, config: Config) -> tuple[str, str] | None:
    """
    A helper function to check if a given name matches any forced separate pattern in the configuration.
    
    Parameters:
        name (str): The string to be checked against the forced separate patterns.
        config (Config): An instance of Config containing the list of forced separate patterns.
        
    Returns:
        tuple[str, str] | None: A tuple containing the matched forced separate pattern and a confirmation message if a match is found, otherwise returns None.
    
    Examples:
        >>> # Assuming config has ['*.log', 'data.*'] as forced_separate patterns
        >>> _forced_separate('example.log', config)
        ('*.log', 'Matched forced_separate (*).log config value.')
        
        >>> _forced_separate('example.txt', config)
        None
        
        >>> # Testing with a different pattern in the config
        >>> config.forced_separate = ['logs/*']
        >>> _forced_separate('logs/app.log', config)
        ('logs/*', 'Matched forced_separate (logs/*) config value.')
    """
    for forced_separate in config.forced_separate:
        # Ensure all forced_separate patterns will match to end of string
        path_glob = forced_separate
        if not forced_separate.endswith("*"):
            path_glob = f"{forced_separate}*"

        if fnmatch(name, path_glob) or fnmatch(name, "." + path_glob):
            return (forced_separate, f"Matched forced_separate ({forced_separate}) config value.")

    return None

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_isort_place__forced_separate_0_test_error_case
isort/Test4DT_tests/test_isort_place__forced_separate_0_test_error_case.py:35:11: E1102: fnmatch is not callable (not-callable)
isort/Test4DT_tests/test_isort_place__forced_separate_0_test_error_case.py:35:39: E1102: fnmatch is not callable (not-callable)


"""