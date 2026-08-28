
import pytest
from ansible.module_utils.splitter import _count_jinja2_blocks


def test_count_jinja2_blocks_unbalanced():
    token = "{{ block1 }} {{ block2 }} {{"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 1

def test_count_jinja2_blocks_empty():
    token = "{{ block1 }} {{ block2 }} }}"
    cur_depth = 0
    open_token = "{{"
    close_token = "}}"
    
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0