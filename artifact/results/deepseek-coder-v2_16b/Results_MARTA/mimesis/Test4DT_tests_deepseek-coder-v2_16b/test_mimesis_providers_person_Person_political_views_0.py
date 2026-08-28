
import pytest
from mimesis.providers.person import Person as MPerson


def test_invalid_locale():
    with pytest.raises(Exception):
        MPerson(locale='unsupported_locale', seed=42)