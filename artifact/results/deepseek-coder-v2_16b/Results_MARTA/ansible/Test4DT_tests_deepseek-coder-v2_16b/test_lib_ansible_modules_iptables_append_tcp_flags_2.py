
import pytest
from ansible.modules.iptables import append_tcp_flags

# Test Case 1: Basic Usage
def test_append_tcp_flags_basic():
    rule = ['initial', 'element']
    param = {'flags': ['SYN'], 'flags_set': ['ACK']}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == ['initial', 'element', 'TCP', 'SYN', 'ACK']

# Test Case 2: No Flags Set
def test_append_tcp_flags_no_flags():
    rule = ['initial', 'element']
    param = {}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == ['initial', 'element']

# Test Case 3: Only Flags Set
def test_append_tcp_flags_only_flags():
    rule = []
    param = {'flags': ['SYN'], 'flags_set': ['ACK']}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == ['TCP', 'SYN', 'ACK']

# Test Case 4: No Parameters Provided
def test_append_tcp_flags_no_params():
    rule = []
    param = {}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == []
