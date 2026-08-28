
import pytest
from ansible.modules.iptables import append_wait

def test_append_wait_with_truthy_param():
    rule = []
    param = 'new'
    flag = 'additional'
    expected_output = ['additional', 'new']
    
    append_wait(rule, param, flag)
    assert rule == expected_output

def test_append_wait_with_falsy_param():
    rule = []
    param = None
    flag = 'start'
    expected_output = []
    
    append_wait(rule, param, flag)
    assert rule == expected_output
