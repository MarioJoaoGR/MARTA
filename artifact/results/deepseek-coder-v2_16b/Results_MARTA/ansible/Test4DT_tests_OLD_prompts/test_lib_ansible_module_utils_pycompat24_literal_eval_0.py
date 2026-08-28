
import pytest
from ansible.module_utils.pycompat24 import literal_eval
import ast

def test_valid_case_string():
    with pytest.raises(ValueError):
        result = literal_eval('1 + 2')
