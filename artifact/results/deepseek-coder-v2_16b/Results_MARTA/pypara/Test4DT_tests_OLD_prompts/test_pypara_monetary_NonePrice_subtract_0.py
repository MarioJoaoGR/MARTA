
import pytest
from pypara.monetary import NonePrice, Price


def test_invalid_subtract():
    with pytest.raises(TypeError):
        NonePrice().subtract("not a Price")