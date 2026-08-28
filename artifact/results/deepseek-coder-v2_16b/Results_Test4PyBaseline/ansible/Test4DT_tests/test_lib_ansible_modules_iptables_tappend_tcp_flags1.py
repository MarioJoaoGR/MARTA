
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
    flag = 'RST'
    append_tcp_flags(rule, param, flag)