
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale

# Test initialization with a valid locale

# Test initialization with an unsupported locale
def test_init_with_unsupported_locale():
    with pytest.raises(UnsupportedLocale):
        Text(locale='es-ES')

# Test words method with default quantity

# Test words method with specified quantity