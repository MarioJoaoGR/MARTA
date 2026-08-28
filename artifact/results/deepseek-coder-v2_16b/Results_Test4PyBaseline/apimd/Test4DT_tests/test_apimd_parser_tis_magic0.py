# Module: apimd.parser
# test_is_magic.py
from apimd.parser import is_magic

def test_is_magic_true():
    assert is_magic('__init__')
    assert is_magic('str.__add__')

def test_is_magic_false():
    assert not is_magic('my_function')
    assert not is_magic('__main__.py')
