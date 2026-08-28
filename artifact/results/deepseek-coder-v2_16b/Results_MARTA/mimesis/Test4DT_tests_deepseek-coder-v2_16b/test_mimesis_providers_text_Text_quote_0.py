
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with specified locale only
def test_specified_locale():
    with pytest.raises(UnsupportedLocale):
        text_data = Text(locale='es-ES')

# Test initialization without specifying any parameters (should raise TypeError)