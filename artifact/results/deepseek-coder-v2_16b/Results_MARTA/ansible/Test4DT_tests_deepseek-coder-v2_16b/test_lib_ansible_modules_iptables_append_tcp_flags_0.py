
import pytest

def append_tcp_flags(rule, param, flag):
    if param:
        if 'flags' in param and 'flags_set' in param:
            rule.extend([flag, ','.join(param['flags']), ','.join(param['flags_set'])])

# Test cases
def test_valid_case():
    rule = ['initial', 'element']
    param = {'flags': ['SYN'], 'flags_set': ['ACK']}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == ['initial', 'element', 'TCP', 'SYN', 'ACK']

def test_edge_case():
    rule = []
    param = {}
    flag = 'TCP'
    append_tcp_flags(rule, param, flag)
    assert rule == []

def test_error_case():
    rule = ['initial', 'element']
    param = {'flags': 123, 'flags_set': [True]}
    flag = 'TCP'
    with pytest.raises(TypeError):
        append_tcp_flags(rule, param, flag)
