
# Module: ansible.utils.version
import pytest
from ansible.utils.version import _Alpha, _Numeric

# Test creating instances of _Alpha class
def test_alpha_instance():
    alpha1 = _Alpha("test")
    assert isinstance(alpha1, _Alpha), "Instance should be an instance of _Alpha"
    
    alpha2 = _Alpha("test")
    assert alpha1 == alpha2, "Instances with the same specifier should be equal"
    
    alpha3 = _Alpha("testing")
    assert alpha1 != alpha3, "Instances with different specifiers should not be equal"
    
    # Test comparison operations
    def test_comparison():
        alpha1 = _Alpha("test")
        alpha2 = _Alpha("test")
        alpha3 = _Alpha("testing")
        
        assert alpha1 == alpha2, "Instances with the same specifier should be equal"
        assert alpha1 != alpha3, "Instances with different specifiers should not be equal"
        
        # Test less than (<) operation
        assert alpha1 < alpha3, "'test' should be less than 'testing'"
        
        # Test greater than (>) operation
        assert alpha3 > alpha1, "'testing' should be greater than 'test'"
        
        # Test less than or equal to (<=) operation
        assert alpha1 <= alpha2, "Instances with the same specifier should satisfy <= comparison"
        assert alpha1 <= alpha3, "'test' should be less than or equal to 'testing'"
        
        # Test greater than or equal to (>=) operation
        assert alpha2 >= alpha1, "Instances with the same specifier should satisfy >= comparison"
        assert alpha3 >= alpha1, "'testing' should be greater than or equal to 'test'"
    
    test_comparison()

# Additional tests for __lt__ method uncovered lines
def test_alpha_less_than():
    alpha1 = _Alpha("test")
    alpha2 = _Alpha("test")
    alpha3 = _Alpha("testing")
    
    assert not (alpha1 < alpha1), "An instance should not be less than itself"
    assert alpha1 < alpha3, "'test' should be less than 'testing'"
    with pytest.raises(ValueError):
        alpha1 < 123, "Comparing with a non-supported type should raise ValueError"

# Additional test for error handling in __lt__ method
def test_alpha_comparison_errors():
    alpha1 = _Alpha("test")
    
    with pytest.raises(ValueError):
        alpha1 < None, "Comparing with None should raise ValueError"
    with pytest.raises(ValueError):
        alpha1 < [], "Comparing with an empty list should raise ValueError"
