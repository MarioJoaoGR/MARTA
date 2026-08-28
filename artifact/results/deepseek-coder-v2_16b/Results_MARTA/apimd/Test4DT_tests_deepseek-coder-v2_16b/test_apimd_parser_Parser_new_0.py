
import pytest
from apimd.parser import Parser


def test_invalid_initialization():
    with pytest.raises(TypeError):
        Parser.new()