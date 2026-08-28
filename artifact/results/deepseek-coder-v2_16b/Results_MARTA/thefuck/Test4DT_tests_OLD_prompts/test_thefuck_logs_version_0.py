
import pytest
from unittest.mock import patch
import sys

def version(thefuck_version, python_version, shell_info):
    sys.stderr.write(
        u'The Fuck {} using Python {} and {}\n'.format(thefuck_version,
                                                       python_version,
                                                       shell_info))

# Test cases for version function
def test_version_function():
    with patch('sys.stderr.write'):
        version("3.24", "3.8", "bash")

def test_version_function_with_variables():
    fuck_version = "3.24"
    python_version = "3.8"
    shell_info = "bash"
    with patch('sys.stderr.write'):
        version(fuck_version, python_version, shell_info)

# Run the tests
if __name__ == "__main__":
    pytest.main()
