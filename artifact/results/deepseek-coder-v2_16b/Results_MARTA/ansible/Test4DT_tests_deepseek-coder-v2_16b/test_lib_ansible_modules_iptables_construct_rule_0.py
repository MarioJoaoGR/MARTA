
import pytest
from ansible.modules.iptables import construct_rule

def append_wait(rule, wait, flag):
    if wait:
        rule.append(flag)

def append_param(rule, param, flag, is_match=True):
    if param:
        if is_match and not any(x for x in rule if '-m' in str(x)):
            rule.append('-m')
        rule.append(flag)
        if isinstance(param, dict):
            for k, v in param.items():
                rule.append(f'--{k} {v}')
        else:
            rule.append(str(param))

def append_tcp_flags(rule, tcp_flags, flag):
    if tcp_flags:
        rule.append(flag)
        for k, v in tcp_flags.items():
            rule.append(f'--{k} {" ".join(v)}')

def append_jump(rule, jump, default_jump='ACCEPT'):
    if jump is None:
        rule.append('-j', default_jump)
    else:
        rule.append('-j', jump)

def test_valid_inputs():
    params = {
        'wait': True,
        'protocol': '-p tcp',
        'source': '-s 192.168.1.0/24',
        'destination': '-d 10.0.0.0/8',
        'match': '-m state --state NEW',
        'tcp_flags': {'flags': ['SYN'], 'flags_set': ['ACK']},
        'jump': 'ACCEPT',
        'log_prefix': '--log-prefix "MyLog"',
        'comment': 'MyComment'
    }
    rule = construct_rule(params)
    assert rule == [
        '-w', '-p tcp', '-s 192.168.1.0/24', '-d 10.0.0.0/8', '-m state --state NEW', '--tcp-flags SYN ACK', 'ACCEPT', '--log-prefix "MyLog"', '--comment "MyComment"'
    ]

def test_edge_cases():
    params = {
        'wait': None,
        'protocol': '',
        'source': '-s 0.0.0.0/0',
        'destination': '-d 255.255.255.255',
        'match': '-m state --state INVALID',
        'tcp_flags': {},
        'jump': None,
        'log_prefix': '',
        'comment': ''
    }
    rule = construct_rule(params)
    assert rule == [
        '--source 0.0.0.0/0', '-d 255.255.255.255', '-m state --state INVALID'
    ]

def test_invalid_inputs():
    params = {
        'wait': True,
        'protocol': '-p udp',
        'source': '-s 172.16.0.0/16',
        'destination': '-d 8.8.8.8',
        'match': '-m tcp --tcp-flags SYN,FIN SYN,FIN',
        'jump': 'DROP',
        'log_prefix': '--log-prefix "NetworkTraffic"',
        'log_level': '--log-level 4'
    }
    with pytest.raises(ValueError):
        construct_rule(params)
