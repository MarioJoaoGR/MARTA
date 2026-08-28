
import pytest
from blib2to3.pgen2.tokenize import generate_tokens, GoodTokenInfo
from typing import Callable, Iterator, Text, Optional
from blib2to3.pgen2.grammar import Grammar


def test_edge_case_none():
    with pytest.raises(TypeError):
        generate_tokens()
