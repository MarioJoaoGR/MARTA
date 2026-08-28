
import pytest
from blib2to3.pgen2.tokenize import _get_normal_name


def test_nonStandardEncoding():
    assert _get_normal_name("utf-8-variant") == "utf-8"

def test_latin1Encoding():
    assert _get_normal_name("latin-1") == "iso-8859-1"

def test_isoLatin1Encoding():
    assert _get_normal_name("ISO-Latin-1") == "iso-8859-1"

def test_standardEncoding():
    assert _get_normal_name("UTF-8") == "utf-8"