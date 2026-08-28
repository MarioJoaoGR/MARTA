
import pytest
from ansible.playbook.play import Play
import copy

@pytest.fixture
def play():
    return Play()

# Test case for ensuring that the copy method returns a deep copy of the instance
def test_copy_method(play):
    original = play
    copied = original.copy()
    assert id(original) != id(copied)  # Ensure different memory location
    assert original.__dict__ == copied.__dict__  # Ensure all attributes are equal

# Test case to check if the role cache is correctly deep copied
def test_role_cache_deep_copy(play):
    original = play.ROLE_CACHE
    copied = play.copy().ROLE_CACHE
    assert id(original) != id(copied)  # Ensure different memory location
    assert original == copied  # Ensure the content is the same

# Test case to check if included conditional is correctly deep copied
def test_included_conditional_deep_copy(play):
    original = play._included_conditional
    copied = play.copy()._included_conditional