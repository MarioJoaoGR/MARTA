
import pytest
from ansible.parsing.splitter import join_args

def test_join_args_multiple_parts():
    assert join_args(['ls', '-l']) == 'ls -l'

def test_join_args_no_special_chars():
    assert join_args(['echo', 'Hello World']) == 'echo Hello World'

def test_join_args_with_newline():
    assert join_args(['dir', '\n']) == 'dir \n'
