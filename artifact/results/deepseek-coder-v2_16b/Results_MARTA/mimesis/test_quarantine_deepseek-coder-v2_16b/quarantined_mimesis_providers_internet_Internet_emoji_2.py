
import pytest
from mimesis.providers.internet import Internet
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

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_internet_Internet_emoji_2.py F [100%]

=================================== FAILURES ===================================
______________________ test_invalid_locale_initialization ______________________

    def test_invalid_locale_initialization():
        with pytest.raises(UnsupportedLocale):
>           internet = Internet(locale="unsupported_locale")

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_internet_Internet_emoji_2.py:8: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.internet.Internet object at 0x7fbcb165e050>, args = ()
kwargs = {'locale': 'unsupported_locale'}

    def __init__(self, *args, **kwargs):
        """Initialize attributes.
    
        :param args: Arguments.
        :param kwargs: Keyword arguments.
        """
>       super().__init__(*args, **kwargs)
E       TypeError: BaseProvider.__init__() got an unexpected keyword argument 'locale'

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/internet.py:38: TypeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_internet_Internet_emoji_2.py::test_invalid_locale_initialization
============================== 1 failed in 0.13s ===============================
"""