
import pytest
from ansible.plugins.filter.urls import do_urldecode

def test_do_urldecode_basic():
    assert do_urldecode("Hello%20World") == "Hello World"

def test_do_urldecode_chinese_chars():
    assert do_urldecode("%E4%B8%AD%E6%96%87") == "中文"
