
import pytest
from blib2to3.pytree import WildcardPattern

HUGE = 2147483647  # Assuming HUGE is a placeholder for the largest possible integer value


def test_specific_content():
    subpattern = WildcardPattern(content=[[1, 2, 3]], min=1, max=HUGE)
    assert isinstance(subpattern.content, tuple)
    assert len(subpattern.content) == 1
    assert all(isinstance(alt, tuple) for alt in subpattern.content)
    assert all(len(alt) > 0 for alt in subpattern.content)


def test_specific_type_and_content():
    with pytest.raises(TypeError):
        specific_nodes = [WildcardPattern(type=257, content=["a", "b"]), WildcardPattern(type=257, content=["c", "d"])]

def test_specific_content_pattern():
    with pytest.raises(TypeError):
        specific_nodes = [WildcardPattern(type=257, content="example_pattern"), WildcardPattern(type=258, content="another_pattern")]

def test_specific_type_pattern():
    with pytest.raises(TypeError):
        specific_nodes = [WildcardPattern(type=257, content=None), WildcardPattern(type=258, content=None)]