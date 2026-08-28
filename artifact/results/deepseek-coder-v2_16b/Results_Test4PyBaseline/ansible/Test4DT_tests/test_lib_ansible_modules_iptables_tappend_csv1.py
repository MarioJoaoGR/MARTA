
import pytest
from ansible.modules.iptables import append_csv

# Test cases for the append_csv function

def test_append_csv_with_valid_params():
    rule = []
    append_csv(rule, ['a', 'b', 'c'], 'example')
    assert rule == ['example', 'a,b,c']

def test_append_csv_with_none_param():
    rule = []
    append_csv(rule, None, 'flag')