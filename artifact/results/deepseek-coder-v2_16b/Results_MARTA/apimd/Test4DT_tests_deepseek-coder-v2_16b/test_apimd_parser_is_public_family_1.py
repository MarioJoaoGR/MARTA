
import pytest
from apimd.parser import is_public_family

def test_valid_case_1():
    assert is_public_family('os') == True

def test_valid_case_2():
    assert is_public_family('os.path') == True

def test_invalid_case():
    assert is_public_family('sys._abc') == False
