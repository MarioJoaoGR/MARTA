
import pytest
from apimd.parser import esc_underscore

def test_single_underscore():
    result = esc_underscore("single_underscore")
    assert result == "single_underscore"



def test_only_underscores():
    result = esc_underscore("________")
    assert result == r"\_\_\_\_\_\_\_\_"
