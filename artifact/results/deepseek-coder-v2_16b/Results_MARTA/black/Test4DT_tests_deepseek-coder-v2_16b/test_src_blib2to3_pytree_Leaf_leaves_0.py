
import pytest
from blib2to3.pytree import Leaf
from typing import Text, Optional, List, Any, Set, Iterator



def test_invalid_input():
    with pytest.raises(AssertionError):
        leaf = Leaf(type=-1, value='error', context=(None, 0, 0))