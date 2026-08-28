
import pytest
from ansible.plugins.filter.core import regex_escape
from ansible.errors import AnsibleFilterError



def test_invalid_input_re_type():
    string = 'Example'
    with pytest.raises(AnsibleFilterError):
        regex_escape(string, re_type='invalid_type')