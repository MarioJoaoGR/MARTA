
import pytest
import sys
from unittest.mock import patch

def compat_conf(conf):
    if sys.version_info < (3,):
        return [a.decode('utf-8', 'replace') for a in conf]
    return conf

@pytest.fixture
def setup_valid_input_python2():
    return ['example1', 'example2']

@pytest.fixture
def setup_valid_input_python3():
    return [b'example1', b'example2']

@pytest.fixture
def setup_empty_list():
    return []

def test_valid_input_python2(setup_valid_input_python2):
    conf = compat_conf(setup_valid_input_python2)
    assert conf == ['example1', 'example2']

def test_valid_input_python3(setup_valid_input_python3):
    conf = compat_conf(setup_valid_input_python3)
    assert conf == [b'example1', b'example2']

def test_empty_list(setup_empty_list):
    conf = compat_conf(setup_empty_list)
    assert conf == []
