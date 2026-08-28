
import pytest
from mimesis.providers.person import Person as MimesisPerson


def test_invalid_locale():
    # Test with invalid locale parameter
    with pytest.raises(Exception):
        person = MimesisPerson(locale='unsupported_locale', seed=42)