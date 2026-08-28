
import pytest
from ansible.utils.version import _Alpha

def test_alpha_comparison():
    alpha1 = _Alpha(None)
    alpha2 = _Alpha('')
    alpha3 = _Alpha(10)
    
    # None comparison should raise TypeError
    with pytest.raises(TypeError):
        assert alpha1 < alpha2

    # Empty string comparison
    assert not (alpha2 == alpha1)

    # Integer comparison
    with pytest.raises(TypeError):
        assert alpha1 < alpha3

