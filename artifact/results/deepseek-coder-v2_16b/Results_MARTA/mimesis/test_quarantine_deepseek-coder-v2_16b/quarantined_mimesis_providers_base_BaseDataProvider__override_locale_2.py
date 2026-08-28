
import pytest
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale

# Test initialization with specified locale and seed

# Test initialization with specified locale only

# Test initialization with no locale and valid seed
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_2.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
________________________ test_specified_locale_and_seed ________________________

    def test_specified_locale_and_seed():
>       base_data_provider = BaseDataProvider(locale="en_US", seed=42)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_2.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.base.BaseDataProvider object at 0x7f67f3a37550>
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
________________________ test_valid_locale_and_no_seed _________________________

    def test_valid_locale_and_no_seed():
>       base_data_provider = BaseDataProvider(locale="en_US")

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_2.py:14: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.base.BaseDataProvider object at 0x7f67f3aabfa0>
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
________________________ test_no_locale_and_valid_seed _________________________

    def test_no_locale_and_valid_seed():
        base_data_provider = BaseDataProvider(seed=42)
>       assert not hasattr(base_data_provider, 'locale')
E       AssertionError: assert not True
E        +  where True = hasattr(<mimesis.providers.base.BaseDataProvider object at 0x7f67f3ab7d30>, 'locale')

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_2.py:21: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_2.py::test_specified_locale_and_seed
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_2.py::test_valid_locale_and_no_seed
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__override_locale_2.py::test_no_locale_and_valid_seed
============================== 3 failed in 0.15s ===============================
"""