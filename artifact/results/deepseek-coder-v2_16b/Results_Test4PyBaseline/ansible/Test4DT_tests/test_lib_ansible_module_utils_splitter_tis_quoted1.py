
# Module: ansible.module_utils.splitter
from ansible.module_utils.splitter import is_quoted

def test_is_quoted_unquoted():
    assert not is_quoted("Hello, World!")
    assert not is_quoted('Hello, World!')

def test_is_quoted_empty_string():
    assert not is_quoted("")