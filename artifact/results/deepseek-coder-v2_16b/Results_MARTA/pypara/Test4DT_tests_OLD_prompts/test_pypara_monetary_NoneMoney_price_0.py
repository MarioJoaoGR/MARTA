
import pytest
from unittest.mock import MagicMock, patch
from pypara.monetary import NoPrice, NoneMoney


def test_invalid_input():
    nm = NoneMoney()
    with pytest.raises(TypeError):
        nm.price()