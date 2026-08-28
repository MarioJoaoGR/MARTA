
import pytest
from blib2to3.pgen2.literals import evalString

def test_eval_string_for_all_ascii_characters():
    for i in range(256):
        c = chr(i)
        s = repr(c)
        e = evalString(s)
        assert e == c, f"Failed for ASCII character {chr(i)} (code {i})"
