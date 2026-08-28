
import pytest
from ansible.utils.version import LooseVersion

class _Alpha:
    """Class to easily allow comparing strings.

    Largely this exists to make comparing an integer and a string on py3 so that it works like py2.

    Parameters:
        specifier (str): The string to be compared with other strings or integers.

    Examples:
        >>> alpha1 = _Alpha("test")
        >>> alpha2 = _Alpha("example")
        >>> print(alpha1 == alpha2)  # False, because "test" != "example"
        
        >>> alpha3 = _Alpha("2")
        >>> alpha4 = _Alpha("3")
        >>> print(alpha3 < alpha4)  # True, because "2" (as integer) is less than "3"
    """
    def __init__(self, specifier):
        self.specifier = str(specifier) if specifier else ''

    def __eq__(self, other):
        if isinstance(other, _Alpha):
            return LooseVersion(self.specifier) == LooseVersion(other.specifier)
        elif isinstance(other, str):
            return LooseVersion(self.specifier) == LooseVersion(other)
        else:
            raise TypeError("Comparison with non-string/non-integer types is not supported.")

    def __ne__(self, other):
        return not self.__eq__(other)

# Test scenarios
def test_valid_inputs():
    alpha1 = _Alpha('2')
    alpha2 = _Alpha('3')
    alpha3 = _Alpha('10')
    
    assert alpha1 < alpha2, "alpha1 should be less than alpha2"
    assert not (alpha1 > alpha2), "alpha1 should not be greater than alpha2"
    assert alpha2 > alpha1, "alpha2 should be greater than alpha1"
    assert not (alpha2 < alpha1), "alpha2 should not be less than alpha1"
    
    assert alpha1 <= alpha3, "alpha1 should be less than or equal to alpha3"
    assert alpha3 >= alpha1, "alpha3 should be greater than or equal to alpha1"

def test_edge_cases():
    alpha_none = _Alpha(None)
    alpha_empty = _Alpha('')
    alpha_maxint = _Alpha('2147483647')
    
    with pytest.raises(TypeError):
        assert alpha_none == None, "alpha_none should not be equal to None"
        
    with pytest.raises(TypeError):
        assert alpha_empty == '', "alpha_empty should not be equal to an empty string"
        
    with pytest.raises(TypeError):
        assert alpha_maxint == 2147483647, "alpha_maxint should not be equal to the integer 2147483647"

def test_invalid_inputs():
    alpha_str = _Alpha('test')
    alpha_int = 123
    
    with pytest.raises(TypeError):
        assert alpha_str == alpha_int, "alpha_str should not be equal to alpha_int"
