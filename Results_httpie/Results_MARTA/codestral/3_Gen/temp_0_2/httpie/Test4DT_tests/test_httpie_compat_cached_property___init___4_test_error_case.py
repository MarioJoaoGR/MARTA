
import pytest
from unittest.mock import patch
from httpie.compat import cached_property

def test_error_case():
    with patch('httpie.compat.cached_property.__init__', side_effect=TypeError):
        with pytest.raises(TypeError):
            cached_property()  # This should raise TypeError as per the mock setup
