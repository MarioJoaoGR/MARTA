
import pytest
from flutes.iterator import take
from unittest.mock import patch, MagicMock



def test_take_negative_n():
    with pytest.raises(ValueError):
        n = -1
        result = list(take(n, range(1000000)))