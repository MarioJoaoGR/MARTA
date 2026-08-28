
import pytest
from datetime import date
from pypara.exchange import Currency, FXRateLookupError


def test_fxratelookuperror_init_invalid():
    with pytest.raises(TypeError):
        FXRateLookupError()