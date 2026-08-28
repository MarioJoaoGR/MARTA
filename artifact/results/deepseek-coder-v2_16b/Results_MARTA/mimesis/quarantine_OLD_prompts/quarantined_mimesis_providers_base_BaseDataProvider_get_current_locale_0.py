
import pytest
from mimesis.providers.base import BaseProvider, locales
from unittest.mock import patch

class BaseDataProvider(BaseProvider):
    def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: int = None) -> None:
        super().__init__(seed=seed)
        self._data: dict = {}
        self._datafile = ''
        self._setup_locale(locale)
        self._data_dir = Path(__file__).parent.parent.joinpath('data')

    def get_current_locale(self) -> str:
        return self.locale if hasattr(self, 'locale') else locales.DEFAULT_LOCALE

@pytest.fixture
def base_data_provider():
    return BaseDataProvider()

@pytest.fixture
def base_data_provider_with_locale():
    return BaseDataProvider(locale="es")




"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 4 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py F [ 25%]
FFF                                                                      [100%]

=================================== FAILURES ===================================
_____________________________ test_default_locale ______________________________

mock_locales = <MagicMock name='locales' id='140446781744096'>

    @patch('mimesis.providers.base.locales')
    def test_default_locale(mock_locales):
        mock_locales.DEFAULT_LOCALE = 'en'
>       provider = BaseDataProvider()

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.BaseDataProvider object at 0x7fbc508923b0>
locale = 'en', seed = None

    def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: int = None) -> None:
        super().__init__(seed=seed)
        self._data: dict = {}
        self._datafile = ''
>       self._setup_locale(locale)
E       AttributeError: 'BaseDataProvider' object has no attribute '_setup_locale'

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py:11: AttributeError
_____________________________ test_specific_locale _____________________________

mock_locales = <MagicMock name='locales' id='140446782125968'>

    @patch('mimesis.providers.base.locales')
    def test_specific_locale(mock_locales):
        mock_locales.DEFAULT_LOCALE = 'en'
>       provider = BaseDataProvider(locale="es")

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.BaseDataProvider object at 0x7fbc508eda80>
locale = 'es', seed = None

    def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: int = None) -> None:
        super().__init__(seed=seed)
        self._data: dict = {}
        self._datafile = ''
>       self._setup_locale(locale)
E       AttributeError: 'BaseDataProvider' object has no attribute '_setup_locale'

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py:11: AttributeError
______________________________ test_default_seed _______________________________

mock_locales = <MagicMock name='locales' id='140446782001920'>

    @patch('mimesis.providers.base.locales')
    def test_default_seed(mock_locales):
        mock_locales.DEFAULT_LOCALE = 'en'
>       provider = BaseDataProvider()

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py:40: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.BaseDataProvider object at 0x7fbc508d1630>
locale = 'en', seed = None

    def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: int = None) -> None:
        super().__init__(seed=seed)
        self._data: dict = {}
        self._datafile = ''
>       self._setup_locale(locale)
E       AttributeError: 'BaseDataProvider' object has no attribute '_setup_locale'

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py:11: AttributeError
______________________________ test_specific_seed ______________________________

mock_locales = <MagicMock name='locales' id='140446782290480'>

    @patch('mimesis.providers.base.locales')
    def test_specific_seed(mock_locales):
        mock_locales.DEFAULT_LOCALE = 'en'
>       provider = BaseDataProvider(seed=12345)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py:46: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.BaseDataProvider object at 0x7fbc50916200>
locale = 'en', seed = 12345

    def __init__(self, locale: str = locales.DEFAULT_LOCALE, seed: int = None) -> None:
        super().__init__(seed=seed)
        self._data: dict = {}
        self._datafile = ''
>       self._setup_locale(locale)
E       AttributeError: 'BaseDataProvider' object has no attribute '_setup_locale'

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py:11: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py::test_default_locale
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py::test_specific_locale
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py::test_default_seed
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider_get_current_locale_0.py::test_specific_seed
============================== 4 failed in 0.11s ===============================
"""