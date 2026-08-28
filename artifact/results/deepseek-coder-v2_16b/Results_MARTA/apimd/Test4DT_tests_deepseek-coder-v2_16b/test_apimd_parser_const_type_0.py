
import pytest
from apimd.parser import const_type, Constant, Tuple, List, Set, Dict, Call, Name, Attribute


def test_valid_constant_node():
    node = Constant(1)
    result = const_type(node)
    assert result == 'int'




