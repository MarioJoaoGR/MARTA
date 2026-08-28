
import pytest
from mimesis.providers.text import Text as MimesisText
from unittest.mock import patch, MagicMock

class TestTextClass:
    @pytest.mark.parametrize("locale", ["en-US", "es-ES"])
    def test_valid_locale(self, locale):
        with patch('mimesis.providers.text.Text._pull', return_value=None):
            text = MimesisText(locale=locale)
            assert isinstance(text, MimesisText)
    
    @pytest.mark.parametrize("locale", [123, None])
    def test_invalid_locale(self, locale):
        with pytest.raises(ValueError):
            MimesisText(locale=locale)
    
    @patch('mimesis.providers.text.Text._pull', return_value=None)
    def test_missing_seed(self, mock_pull):
        text = MimesisText(locale='en-US')
        assert isinstance(text, MimesisText)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
____________________ TestTextClass.test_valid_locale[en-US] ____________________

self = <test_mimesis_providers_text_Text___init___0.TestTextClass object at 0x7f7b27bf7df0>
locale = 'en-US'

    @pytest.mark.parametrize("locale", ["en-US", "es-ES"])
    def test_valid_locale(self, locale):
        with patch('mimesis.providers.text.Text._pull', return_value=None):
>           text = MimesisText(locale=locale)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/text.py:22: in __init__
    super().__init__(*args, **kwargs)
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.text.Text object at 0x7f7b27c465f0>, locale = 'en-us'

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
E           mimesis.exceptions.UnsupportedLocale: Locale «en-us» is not supported

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:101: UnsupportedLocale
____________________ TestTextClass.test_valid_locale[es-ES] ____________________

self = <test_mimesis_providers_text_Text___init___0.TestTextClass object at 0x7f7b27bf7e20>
locale = 'es-ES'

    @pytest.mark.parametrize("locale", ["en-US", "es-ES"])
    def test_valid_locale(self, locale):
        with patch('mimesis.providers.text.Text._pull', return_value=None):
>           text = MimesisText(locale=locale)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/text.py:22: in __init__
    super().__init__(*args, **kwargs)
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.text.Text object at 0x7f7b27c47340>, locale = 'es-es'

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
E           mimesis.exceptions.UnsupportedLocale: Locale «es-es» is not supported

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:101: UnsupportedLocale
____________________ TestTextClass.test_invalid_locale[123] ____________________

self = <test_mimesis_providers_text_Text___init___0.TestTextClass object at 0x7f7b27c443a0>
locale = 123

    @pytest.mark.parametrize("locale", [123, None])
    def test_invalid_locale(self, locale):
        with pytest.raises(ValueError):
>           MimesisText(locale=locale)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/text.py:22: in __init__
    super().__init__(*args, **kwargs)
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.text.Text object at 0x7f7b27c90c70>, locale = 123

    def _setup_locale(self, locale: str = locales.DEFAULT_LOCALE) -> None:
        """Set up locale after pre-check.
    
        :param str locale: Locale
        :raises UnsupportedLocale: When locale not supported.
        :return: Nothing.
        """
        if not locale:
            locale = locales.DEFAULT_LOCALE
    
>       locale = locale.lower()
E       AttributeError: 'int' object has no attribute 'lower'

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:99: AttributeError
___________________ TestTextClass.test_invalid_locale[None] ____________________

self = <test_mimesis_providers_text_Text___init___0.TestTextClass object at 0x7f7b27c44490>
locale = None

    @pytest.mark.parametrize("locale", [123, None])
    def test_invalid_locale(self, locale):
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py:15: Failed
_______________________ TestTextClass.test_missing_seed ________________________

self = <test_mimesis_providers_text_Text___init___0.TestTextClass object at 0x7f7b27c44640>
mock_pull = <MagicMock name='_pull' id='140166925323952'>

    @patch('mimesis.providers.text.Text._pull', return_value=None)
    def test_missing_seed(self, mock_pull):
>       text = MimesisText(locale='en-US')

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/text.py:22: in __init__
    super().__init__(*args, **kwargs)
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.text.Text object at 0x7f7b27cb0f40>, locale = 'en-us'

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
E           mimesis.exceptions.UnsupportedLocale: Locale «en-us» is not supported

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:101: UnsupportedLocale
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py::TestTextClass::test_valid_locale[en-US]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py::TestTextClass::test_valid_locale[es-ES]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py::TestTextClass::test_invalid_locale[123]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py::TestTextClass::test_invalid_locale[None]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text___init___0.py::TestTextClass::test_missing_seed
============================== 5 failed in 0.12s ===============================
"""