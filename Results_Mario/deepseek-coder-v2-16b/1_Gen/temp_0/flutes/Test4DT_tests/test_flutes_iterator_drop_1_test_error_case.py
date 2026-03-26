
import pytest
from flutes.iterator import drop

def test_error_case():
    with pytest.raises(ValueError) as exc_info:
        list(drop(-1, range(10)))
    assert str(exc_info.value) == "`n` should be non-negative"
