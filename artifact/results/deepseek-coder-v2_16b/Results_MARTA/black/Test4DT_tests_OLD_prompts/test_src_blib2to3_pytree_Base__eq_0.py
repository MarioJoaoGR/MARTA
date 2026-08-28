
import pytest
from blib2to3.pytree import Base


def test_invalid_input():
    class MyNode(Base):
        def _eq(self, other: 'MyNode') -> bool:
            return super()._eq(other)
    
    node1 = MyNode()
    with pytest.raises(NotImplementedError):
        assert node1._eq(None) is True