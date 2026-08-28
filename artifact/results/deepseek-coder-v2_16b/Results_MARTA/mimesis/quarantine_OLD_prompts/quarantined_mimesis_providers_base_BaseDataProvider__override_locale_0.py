
import pytest
from unittest.mock import patch
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale

class TestBaseDataProvider:
    
    @patch('mimesis.providers.base.locales')
    def test_valid_locale_and_seed(self, mock_locales):
        # Mock the default locale to return 'en_US'
        mock_locales.DEFAULT_LOCALE = 'en_US'
        
        base_data_provider = BaseDataProvider(locale='en_US', seed=42)
        assert base_data_provider.locale == 'en_US'
    
    @patch('mimesis.providers.base.locales')
    def test_missing_locale(self, mock_locales):
        # Mock the default locale to return None (indicating no locale is provided)
        mock_locales.DEFAULT_LOCALE = None
        
        with pytest.raises(TypeError):
            BaseDataProvider()
    
    @patch('mimesis.providers.base.locales')
    def test_unsupported_locale(self, mock_locales):
        # Mock a locale that is not in SUPPORTED_LOCALES
        mock_locales.DEFAULT_LOCALE = 'en_US'
        mock_locales.SUPPORTED_LOCALES = ['fr_FR', 'es_ES']
        
        with pytest.raises(UnsupportedLocale):
            BaseDataProvider(locale='unsupported_locale')
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_0.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
_______________ TestBaseDataProvider.test_valid_locale_and_seed ________________

self = <test_mimesis_providers_base_BaseDataProvider__override_locale_0.TestBaseDataProvider object at 0x7f1e2ce49b40>
mock_locales = <MagicMock name='locales' id='139767578927184'>

    @patch('mimesis.providers.base.locales')
    def test_valid_locale_and_seed(self, mock_locales):
        # Mock the default locale to return 'en_US'
        mock_locales.DEFAULT_LOCALE = 'en_US'
    
>       base_data_provider = BaseDataProvider(locale='en_US', seed=42)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_0.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.base.BaseDataProvider object at 0x7f1e2ce4bd00>
locale = 'en_us'

    def _setup_locale(self, locale: str = locales.DEFAULT_LOCALE) -> None:
        """Set up locale after pre-check.
    
        :param str locale: Locale
        :raises UnsupportedLocale: When locale not supported.
        :return: Nothing.
        """
        if not locale:
            locale = locales.DEFAULT_LOCALE
    
        locale = locale.lower()
        if locale not in locales.SUPPORTED_LOCALES:
>           raise UnsupportedLocale(locale)
E           mimesis.exceptions.UnsupportedLocale: Locale «en_us» is not supported

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:101: UnsupportedLocale
___________________ TestBaseDataProvider.test_missing_locale ___________________

self = <test_mimesis_providers_base_BaseDataProvider__override_locale_0.TestBaseDataProvider object at 0x7f1e2ce49c00>
mock_locales = <MagicMock name='locales' id='139767579327888'>

    @patch('mimesis.providers.base.locales')
    def test_missing_locale(self, mock_locales):
        # Mock the default locale to return None (indicating no locale is provided)
        mock_locales.DEFAULT_LOCALE = None
    
        with pytest.raises(TypeError):
>           BaseDataProvider()

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.base.BaseDataProvider object at 0x7f1e2cea9d20>
locale = 'en'

    def _setup_locale(self, locale: str = locales.DEFAULT_LOCALE) -> None:
        """Set up locale after pre-check.
    
        :param str locale: Locale
        :raises UnsupportedLocale: When locale not supported.
        :return: Nothing.
        """
        if not locale:
            locale = locales.DEFAULT_LOCALE
    
        locale = locale.lower()
        if locale not in locales.SUPPORTED_LOCALES:
>           raise UnsupportedLocale(locale)
E           mimesis.exceptions.UnsupportedLocale: Locale «en» is not supported

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:101: UnsupportedLocale
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_0.py::TestBaseDataProvider::test_valid_locale_and_seed
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_0.py::TestBaseDataProvider::test_missing_locale
========================= 2 failed, 1 passed in 0.10s ==========================
"""