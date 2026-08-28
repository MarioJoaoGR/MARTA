
import pytest
from flutils.decorators import cached_property

class MyClassWithCacheReset:
    def __init__(self):
        self.x = 5

    @cached_property
    def y(self):
        return self.x + 1

@pytest.fixture
def obj():
    return MyClassWithCacheReset()

def test_initial_access(obj):
    assert obj.y == 6  # Initial access, computation happens
