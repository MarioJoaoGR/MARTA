
import pytest
from ansible.modules.iptables import append_wait

def test_append_wait_with_truthy_param():
    my_list = []
    append_wait(my_list, 'new', 'additional')
    assert my_list == ['additional', 'new']

def test_append_wait_with_falsy_param():
    my_list = []
    append_wait(my_list, None, 'start')
    assert my_list == []
