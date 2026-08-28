
import pytest
from ansible.parsing.splitter import _count_jinja2_blocks

def test_valid_case():
    token = "{% for item in items %}{% endfor %}"
    cur_depth = 0
    open_token = "{%"
    close_token = "%}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0


def test_empty_token():
    token = ""
    cur_depth = 0
    open_token = "{%"
    close_token = "%}"
    result = _count_jinja2_blocks(token, cur_depth, open_token, close_token)
    assert result == 0