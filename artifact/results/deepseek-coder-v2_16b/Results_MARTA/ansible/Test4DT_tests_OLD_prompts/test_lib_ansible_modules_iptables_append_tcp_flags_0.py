
import pytest
from ansible.modules.iptables import append_tcp_flags

def test_append_tcp_flags_with_all_params():
    rule = []
    param = {'flags': ['SYN'], 'flags_set': ['ACK']}
    flag = 'TCP'
    expected_output = ['TCP', 'SYN', 'ACK']
    
    append_tcp_flags(rule, param, flag)
    assert rule == expected_output


def test_append_tcp_flags_with_no_params():
    rule = []
    param = {}
    flag = 'TCP'
    expected_output = []
    
    append_tcp_flags(rule, param, flag)
    assert rule == expected_output