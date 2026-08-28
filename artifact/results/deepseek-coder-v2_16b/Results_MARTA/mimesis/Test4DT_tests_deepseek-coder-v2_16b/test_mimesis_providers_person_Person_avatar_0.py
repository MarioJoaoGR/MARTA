
import pytest
from mimesis import Person
from mimesis.exceptions import UnsupportedLocale

# Test 1: Test avatar generation with default size
def test_valid_avatar_generation():
    person = Person(locale='en')
    avatar_link = person.avatar()
    assert isinstance(avatar_link, str), "Avatar link should be a string"
    assert len(avatar_link) > 0, "Avatar link should not be empty"

# Test 2: Test avatar generation with custom size
def test_custom_avatar_size():
    person = Person(locale='en')
    avatar_link_default = person.avatar()
    avatar_link_custom = person.avatar(size=512)
    assert isinstance(avatar_link_custom, str), "Custom size avatar link should be a string"
    assert len(avatar_link_custom) > 0, "Custom size avatar link should not be empty"
    assert avatar_link_default != avatar_link_custom, "Default and custom size avatars should differ"

# Test 3: Test avatar generation with unsupported locale
def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        person = Person(locale='unsupported_locale')
