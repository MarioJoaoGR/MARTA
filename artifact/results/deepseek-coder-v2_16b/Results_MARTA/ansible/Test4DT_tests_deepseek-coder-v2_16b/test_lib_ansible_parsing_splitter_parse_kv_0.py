
import pytest
from ansible.parsing.splitter import parse_kv

def test_parse_kv_basic():
    result = parse_kv('key1=value1 key2="value with spaces"')
    assert result == {'key1': 'value1', 'key2': 'value with spaces'}

def test_parse_kv_with_check_raw():
    result = parse_kv('arg1=value1 arg2="another value"', check_raw=True)
    assert result == {'_raw_params': 'arg1=value1 arg2="another value"'}

def test_parse_kv_without_check_raw():
    result = parse_kv('creates=file.txt removes=oldfile.txt')
    assert result == {'creates': 'file.txt', 'removes': 'oldfile.txt'}
