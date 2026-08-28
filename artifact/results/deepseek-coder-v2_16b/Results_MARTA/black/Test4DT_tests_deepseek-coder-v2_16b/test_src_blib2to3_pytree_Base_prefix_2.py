
import pytest
from blib2to3.pytree import Base


class MyBase(Base):
    def prefix(self) -> str:
        return "MyPrefix"

def test_error_case():
    class MyBase(Base):
        def prefix(self) -> str:
            return "MyPrefix"
    
    assert issubclass(MyBase, Base), "MyBase must be a subclass of Base"