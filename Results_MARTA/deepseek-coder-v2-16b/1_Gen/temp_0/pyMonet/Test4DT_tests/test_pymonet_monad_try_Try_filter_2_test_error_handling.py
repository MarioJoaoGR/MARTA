
import pytest
from pymonet.monad_try import Try

def test_error_handling():
    none_filterer_try = Try(4, is_success=True)
    
    with pytest.raises(TypeError):
        none_filterer_try.filter(None)
