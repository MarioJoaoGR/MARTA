
import os
from unittest.mock import patch

def session_hostname_to_dirname(hostname: str, session_name: str) -> str:
    """
    Converts a hostname with optional port to a directory name and constructs a JSON file path.
    
    This function takes a hostname (optionally including a port separated by a colon) and a session name, 
    replaces any colons in the hostname with underscores, and then joins the parts into a directory structure 
    under SESSIONS_DIR_NAME. The final part of the path is a JSON file named after the session name.
    
    Parameters:
        hostname (str): The hostname to be processed. It can include a port separated by a colon, e.g., 'example.com:8080'.
        session_name (str): The name of the session which will be used as part of the file name.
    
    Returns:
        str: A string representing the full path to the JSON file for the given session and hostname.
    
    Examples:
        >>> session_hostname_to_dirname('example.com', 'session1')
        '/path/to/sessions/example_com/session1.json'
        
        >>> session_hostname_to_dirname('example.com:8080', 'session2')
        '/path/to/sessions/example_com_8080/session2.json'
    
    Notes:
        - The function assumes that SESSIONS_DIR_NAME is a predefined directory where session data will be stored.
        - This function uses the `os.path.join` method to construct the final path, so make sure the environment allows for this operation.
    """
    hostname = hostname.replace(':', '_')
    return os.path.join(SESSIONS_DIR_NAME, hostname, f'{session_name}.json')

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests_codestral.test_httpie_sessions_session_hostname_to_dirname_0_test_valid_input
httpie/Test4DT_tests_codestral/test_httpie_sessions_session_hostname_to_dirname_0_test_valid_input.py:32:24: E0602: Undefined variable 'SESSIONS_DIR_NAME' (undefined-variable)


"""