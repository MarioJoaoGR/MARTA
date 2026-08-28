
import pytest
from youtube_dl.options import _hide_login_info



def test_empty_input():
    opts = []
    expected = []
    assert _hide_login_info(opts) == expected

def test_no_sensitive_info():
    opts = ['-v', '--verbose']
    expected = ['-v', '--verbose']
    assert _hide_login_info(opts) == expected