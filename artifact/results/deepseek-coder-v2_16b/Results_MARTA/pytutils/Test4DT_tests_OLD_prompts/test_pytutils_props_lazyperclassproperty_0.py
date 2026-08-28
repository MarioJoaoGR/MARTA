
import pytest
from pytutils.props import lazyperclassproperty

def test_valid_case():
    class MyClass:
        pass
    
    def expensive_calculation(cls):
        return [i for i in range(10)]
    
    with pytest.raises(TypeError):
        MyClass = lazyperclassproperty(expensive_calculation)(MyClass)

def test_edge_case():
    class MyClass:
        pass
    
    def expensive_calculation(cls):
        return [i for i in range(10)]
    
    with pytest.raises(TypeError):
        MyClass = lazyperclassproperty(expensive_calculation)(None)
