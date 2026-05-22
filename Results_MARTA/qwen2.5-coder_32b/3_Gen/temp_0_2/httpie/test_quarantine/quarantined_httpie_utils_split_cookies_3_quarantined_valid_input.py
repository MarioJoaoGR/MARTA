
import re
from httpie.utils import RE_COOKIE_SPLIT

def split_cookies(cookies):
    """
    Splits concatenated cookies separated by ``, `` into individual cookie strings.
    
    This function is designed to handle the scenario where multiple cookies are stored in a single header as a comma-separated string. It ensures that each cookie remains intact and not split at commas unless they are part of the actual cookie value.
    
    Parameters:
        cookies (str): A string containing one or more cookies concatenated with ``, ``.
        
    Returns:
        list: A list of individual cookie strings. If no cookies are provided, it returns an empty list.
    
    Examples:
        >>> split_cookies('cookie1=value1, cookie2=value2')
        ['cookie1=value1', 'cookie2=value2']
        
        >>> split_cookies('; path=/; domain=.example.com; Secure')
        ['; path=/; domain=.example.com; Secure']
        
        >>> split_cookies('')
        []
    """
    if not cookies:
        return []
    return RE_COOKIE_SPLIT.split(cookies)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_qwen2.5-coder_32b.json
============================ no tests ran in 0.15s =============================
"""