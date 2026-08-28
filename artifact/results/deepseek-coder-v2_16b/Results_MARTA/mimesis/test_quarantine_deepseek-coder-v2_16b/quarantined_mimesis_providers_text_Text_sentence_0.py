
import pytest
from mimesis.providers.text import Text
from mimesis.exceptions import UnsupportedLocale



"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
______________________ test_valid_input_default_quantity _______________________

    def test_valid_input_default_quantity():
>       text_data = Text(locale='en-US')

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/text.py:22: in __init__
    super().__init__(*args, **kwargs)
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.text.Text object at 0x7fd15fd69c00>, locale = 'en-us'

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
_____________________ test_valid_input_specified_quantity ______________________

    def test_valid_input_specified_quantity():
>       text_data = Text(locale='en-US', quantity=3)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.text.Text object at 0x7fd1600fb040>, args = ()
kwargs = {'locale': 'en-US', 'quantity': 3}

    def __init__(self, *args, **kwargs):
        """Initialize attributes.
    
        :param locale: Current locale.
        :param seed: Seed.
        """
>       super().__init__(*args, **kwargs)
E       TypeError: BaseDataProvider.__init__() got an unexpected keyword argument 'quantity'

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/text.py:22: TypeError
_____________________ test_invalid_input_negative_quantity _____________________

    def test_invalid_input_negative_quantity():
        with pytest.raises(ValueError):
>           Text(locale='en-US', quantity=-1)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_0.py:17: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.text.Text object at 0x7fd15fd6b7c0>, args = ()
kwargs = {'locale': 'en-US', 'quantity': -1}

    def __init__(self, *args, **kwargs):
        """Initialize attributes.
    
        :param locale: Current locale.
        :param seed: Seed.
        """
>       super().__init__(*args, **kwargs)
E       TypeError: BaseDataProvider.__init__() got an unexpected keyword argument 'quantity'

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/text.py:22: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_0.py::test_valid_input_default_quantity
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_0.py::test_valid_input_specified_quantity
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_text_Text_sentence_0.py::test_invalid_input_negative_quantity
============================== 3 failed in 0.12s ===============================
"""