
import pytest
from ansible.utils.version import _Alpha

# Test valid inputs
def test_valid_inputs():
    alpha1 = _Alpha('apple')
    alpha2 = _Alpha('banana')
    alpha3 = _Alpha('10')
    
    assert alpha1 < alpha2, "Expected 'apple' to be less than 'banana'"
    assert not (alpha1 > alpha2), "Expected 'apple' not to be greater than 'banana'"
    assert alpha1 <= alpha2, "Expected 'apple' to be less than or equal to 'banana'"
    assert not (alpha1 >= alpha2), "Expected 'apple' not to be greater than or equal to 'banana'"
    
    assert alpha1 < alpha3, "Expected 'apple' to be less than '10'"
    assert not (alpha1 > alpha3), "Expected 'apple' not to be greater than '10'"
    assert alpha1 <= alpha3, "Expected 'apple' to be less than or equal to '10'"
    assert not (alpha1 >= alpha3), "Expected 'apple' not to be greater than or equal to '10'"
    
    assert alpha2 > alpha1, "Expected 'banana' to be greater than 'apple'"
    assert not (alpha2 < alpha1), "Expected 'banana' not to be less than 'apple'"
    assert alpha2 >= alpha1, "Expected 'banana' to be greater than or equal to 'apple'"
    assert not (alpha2 <= alpha1), "Expected 'banana' not to be less than or equal to 'apple'"
    
    assert alpha3 > alpha1, "Expected '10' to be greater than 'apple'"
    assert not (alpha3 < alpha1), "Expected '10' not to be less than 'apple'"
    assert alpha3 >= alpha1, "Expected '10' to be greater than or equal to 'apple'"
    assert not (alpha3 <= alpha1), "Expected '10' not to be less than or equal to 'apple'"

# Test edge cases
def test_edge_cases():
    alpha_none = _Alpha(None)
    alpha_empty = _Alpha('')
    
    with pytest.raises(TypeError):
        assert alpha_none < alpha_empty, "Expected TypeError when comparing None"
    with pytest.raises(TypeError):
        assert alpha_none > alpha_empty, "Expected TypeError when comparing None"
    with pytest.raises(TypeError):
        assert alpha_none <= alpha_empty, "Expected TypeError when comparing None"
    with pytest.raises(TypeError):
        assert alpha_none >= alpha_empty, "Expected TypeError when comparing None"
    
    with pytest.raises(TypeError):
        assert alpha_empty < alpha_none, "Expected TypeError when comparing empty string to None"
    with pytest.raises(TypeError):
        assert alpha_empty > alpha_none, "Expected TypeError when comparing empty string to None"
    with pytest.raises(TypeError):
        assert alpha_empty <= alpha_none, "Expected TypeError when comparing empty string to None"
    with pytest.raises(TypeError):
        assert alpha_empty >= alpha_none, "Expected TypeError when comparing empty string to None"

# Test invalid inputs
def test_invalid_inputs():
    try:
        _Alpha(123)
    except Exception as e:
        assert isinstance(e, ValueError), "Expected ValueError for invalid input type"
