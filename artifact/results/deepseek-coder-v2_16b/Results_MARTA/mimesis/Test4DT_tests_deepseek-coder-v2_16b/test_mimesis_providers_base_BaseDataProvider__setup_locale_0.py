
import pytest
from mimesis.providers.base import BaseProvider
from mimesis.exceptions import UnsupportedLocale
from pathlib import Path

# Assuming 'locales' and 'Seed' are defined in a module or library used by BaseDataProvider
class BaseDataProvider(BaseProvider):
    def __init__(self, locale: str = 'en_US', seed: int = 42) -> None:
        super().__init__(seed=seed)
        self._data = {}
        self._datafile = ''
        self._setup_locale(locale)
        self._data_dir = Path(__file__).parent.parent.joinpath('data')

    def _setup_locale(self, locale: str = 'en_US') -> None:
        if not locale:
            locale = 'en_US'

        locale = locale.lower()
        if locale not in ['en_us', 'es_ES']:  # Simplified supported locales for example
            raise UnsupportedLocale(locale)

        self.locale = locale

# Test cases
def test_valid_locale():
    base_data_provider = BaseDataProvider(locale='en_US', seed=42)
    assert base_data_provider.locale == 'en_us'

def test_invalid_locale():
    with pytest.raises(UnsupportedLocale):
        base_data_provider = BaseDataProvider(locale='unsupported_locale')

def test_no_locale():
    base_data_provider = BaseDataProvider()
    assert base_data_provider.locale == 'en_us'
