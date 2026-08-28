
import pytest
from unittest.mock import patch
from ansible.modules.iptables import append_wait

def test_append_when_param_is_truthy():
    my_list = [1, 2, 3]
    with patch('builtins.print') as mock_print:
        append_wait(my_list, 'new', 'additional')
        assert my_list == [1, 2, 3, 'additional', 'new']



def test_append_when_param_is_truthy_with_default_flag():
    my_list = []
    with patch('builtins.print') as mock_print:
        append_wait(my_list, 5, 'default')
        assert my_list == ['default', 5]