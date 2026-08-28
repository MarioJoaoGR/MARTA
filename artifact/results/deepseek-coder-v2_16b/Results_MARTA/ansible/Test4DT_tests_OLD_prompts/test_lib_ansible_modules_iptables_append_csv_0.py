
import pytest
from ansible.modules.iptables import append_csv



def test_append_csv_with_empty_list():
    rule = []
    param = ['value1', 'value2']
    flag = 'data'
    expected_output = ['data', 'value1,value2']
    
    append_csv(rule, param, flag)
    assert rule == expected_output
