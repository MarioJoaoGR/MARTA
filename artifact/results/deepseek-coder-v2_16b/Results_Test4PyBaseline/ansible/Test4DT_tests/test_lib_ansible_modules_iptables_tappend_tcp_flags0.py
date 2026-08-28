# Module: ansible.modules.iptables
import pytest
from ansible.modules.iptables import append_tcp_flags

# Test cases for append_tcp_flags function
def test_append_tcp_flags_basic():
    rule = ['existing', 'components']
    param = {'flags': ['SYN'], 'flags_set': ['ACK']}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == ['existing', 'components', 'TCP', 'SYN', 'ACK']

def test_append_tcp_flags_no_flags_or_flags_set():
    rule = ['existing', 'components']
    param = {}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == ['existing', 'components']

def test_append_tcp_flags_only_flags_set():
    rule = []
    param = {'flags_set': ['RST', 'FIN']}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == ['TCP', 'RST', 'FIN']

def test_append_tcp_flags_only_flags():
    rule = []
    param = {'flags': ['SYN']}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == ['TCP', 'SYN']

def test_append_tcp_flags_empty_dictionary():
    rule = []
    param = {}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == []

# Additional edge cases can be added to cover more scenarios
