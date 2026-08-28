
import pytest
from ansible.modules.iptables import append_tcp_flags

def test_append_tcp_flags_basic():
    rule = ['initial', 'element']
    param = {'flags': ['SYN'], 'flags_set': ['ACK']}
    flag = 'TCP'
    expected_output = ['initial', 'element', 'TCP', 'SYN', 'ACK']
    
    append_tcp_flags(rule, param, flag)
    assert rule == expected_output

def test_append_tcp_flags_no_flags():
    rule = ['initial', 'element']
    param = {}
    flag = 'TCP'
    expected_output = ['initial', 'element']
    
    append_tcp_flags(rule, param, flag)
    assert rule == expected_output

def test_append_tcp_flags_only_flags():
    rule = []
    param = {'flags': ['SYN'], 'flags_set': ['ACK']}
    flag = 'TCP'
    expected_output = ['TCP', 'SYN', 'ACK']
    
    append_tcp_flags(rule, param, flag)
    assert rule == expected_output

def test_append_tcp_flags_no_parameters():
    rule = []
    param = {}
    flag = 'TCP'
    expected_output = []
    
    append_tcp_flags(rule, param, flag)
    assert rule == expected_output
