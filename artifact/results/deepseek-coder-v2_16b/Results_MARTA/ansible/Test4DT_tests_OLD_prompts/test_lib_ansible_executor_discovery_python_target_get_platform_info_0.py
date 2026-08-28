
import pytest
from unittest.mock import patch, MagicMock
import platform

def get_platform_info():
    """
    Retrieves platform distribution information and OS release content from system files.

    This function checks if the 'dist' attribute is available on the 'platform' module, which indicates whether it can retrieve platform distribution details. If not, it attempts to read the contents of two specific files: '/etc/os-release' and '/usr/lib/os-release'. These files typically contain information about the operating system distribution.

    Parameters:
        None

    Returns:
        dict: A dictionary containing two keys - 'platform_dist_result' (a list of tuples representing platform distribution details, if available) and 'osrelease_content' (the content of either '/etc/os-release' or '/usr/lib/os-release', whichever is successfully read). If neither file can be read, both values will be set to an empty list and None respectively.

    Example:
        To get the platform distribution information and OS release content, you can call the function like this:
        
        >>> info = get_platform_info()
        >>> print(info)
    
    Notes:
        - The function relies on the 'platform' module to check for the presence of a 'dist' attribute. If this attribute is not available, it will attempt to read from '/etc/os-release' and then fallback to '/usr/lib/os-release'.
        - Both files are assumed to be UTF-8 encoded unless otherwise specified in the function call or documentation for `read_utf8_file`.
    """
    result = dict(platform_dist_result=[])

    if hasattr(platform, 'dist'):
        result['platform_dist_result'] = platform.dist()

    osrelease_content = read_utf8_file('/etc/os-release')
    # try to fall back to /usr/lib/os-release
    if not osrelease_content:
        osrelease_content = read_utf8_file('/usr/lib/os-release')

    result['osrelease_content'] = osrelease_content

    return result

def read_utf8_file(path):
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()

# Test cases for get_platform_info function
@patch('builtins.open', new_callable=lambda: MagicMock(spec=open))
def test_valid_input(mock_open):
    mock_open.return_value.__enter__.return_value.read.side_effect = [
        'NAME="Ubuntu"\nVERSION="20.04"',  # /etc/os-release
        ''  # /usr/lib/os-release (should not be read)
    ]
    
    expected_output = {
        'platform_dist_result': [],
        'osrelease_content': 'NAME="Ubuntu"\nVERSION="20.04"'
    }
    
    assert get_platform_info() == expected_output

