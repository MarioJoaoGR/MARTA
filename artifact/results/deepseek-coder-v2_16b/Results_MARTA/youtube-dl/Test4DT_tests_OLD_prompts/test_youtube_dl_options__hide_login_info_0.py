
import pytest
from unittest.mock import patch
from youtube_dl.options import _hide_login_info



def test_hide_login_info_empty():
    assert _hide_login_info([]) == []
