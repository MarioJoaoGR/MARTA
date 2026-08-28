# Module: blib2to3.pgen2.tokenize
import pytest
from blib2to3.pgen2.tokenize import _get_normal_name

def test__get_normal_name_utf_8():
    assert _get_normal_name("UTF-8") == "utf-8"
    assert _get_normal_name("utf-8") == "utf-8"
    assert _get_normal_name("utf-8-variant") == "utf-8"

def test__get_normal_name_latin_1():
    assert _get_normal_name("latin-1") == "iso-8859-1"
    assert _get_normal_name("ISO-Latin-1") == "iso-8859-1"
    assert _get_normal_name("iso-latin-1") == "iso-8859-1"
    assert _get_normal_name("latin-1-variant") == "iso-8859-1"
    assert _get_normal_name("ISO-Latin-1-variant") == "iso-8859-1"

def test__get_normal_name_other():
    assert _get_normal_name("something-else") == "something-else"
    assert _get_normal_name("another-encoding") == "another-encoding"
