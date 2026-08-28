
import pytest
from unittest.mock import patch
from mimesis.providers.base import BaseDataProvider, locales
from mimesis.exceptions import UnsupportedLocale

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__setup_locale_0.py F [100%]

=================================== FAILURES ===================================
___________________________ test_unsupported_locale ____________________________

    def test_unsupported_locale():
        with patch('mimesis.providers.base.locales.SUPPORTED_LOCALES', new=lambda: ['es']), pytest.raises(UnsupportedLocale):
>           provider = BaseDataProvider()

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__setup_locale_0.py:9: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.base.BaseDataProvider object at 0x7f76a27d79d0>
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
>       if locale not in locales.SUPPORTED_LOCALES:
E       TypeError: argument of type 'function' is not iterable

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:100: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_base_BaseDataProvider__setup_locale_0.py::test_unsupported_locale
============================== 1 failed in 0.09s ===============================
"""