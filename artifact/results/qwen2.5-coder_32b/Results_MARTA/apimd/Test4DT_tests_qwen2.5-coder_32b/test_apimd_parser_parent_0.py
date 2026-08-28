
import pytest
from apimd.parser import parent

def test_happy_path_level_1():
    assert parent('a.b.c.d.e') == 'a.b.c.d'

def test_happy_path_level_2():
    assert parent('a.b.c.d.e', level=2) == 'a.b.c'

def test_happy_path_level_3():
    assert parent('a.b.c.d.e', level=3) == 'a.b'



