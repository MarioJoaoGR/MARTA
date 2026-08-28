
import pytest
from youtube_dl.options import _hide_login_info



def test_hide_login_info_empty():
    opts = []
    expected = []
    assert _hide_login_info(opts) == expected

def test_hide_login_info_no_sensitive_info():
    opts = ['-v', '-f']
    expected = ['-v', '-f']
    assert _hide_login_info(opts) == expected