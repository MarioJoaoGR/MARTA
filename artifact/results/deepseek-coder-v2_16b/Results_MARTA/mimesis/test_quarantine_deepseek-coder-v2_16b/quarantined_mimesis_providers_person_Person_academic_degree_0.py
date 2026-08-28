
import pytest
from mimesis.providers.person import Person as MPerson
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

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_academic_degree_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_________________________ test_valid_case_with_locale __________________________

    def test_valid_case_with_locale():
>       person = MPerson(locale='en_US', seed=42)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_academic_degree_0.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/person.py:36: in __init__
    super().__init__(*args, **kwargs)
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:86: in __init__
    self._setup_locale(locale)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.person.Person object at 0x7faa3a9f0970>
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
_____________________________ test_invalid_locale ______________________________

    def test_invalid_locale():
        with pytest.raises(UnsupportedLocale):
            MPerson(locale='unsupported_locale')
        # Additional assertion to check the error message
        with pytest.raises(UnsupportedLocale) as e:
            MPerson(locale='unsupported_locale')
>       assert str(e.value).startswith('UnsupportedLocale'), "Expected UnsupportedLocale error, got {}".format(str(e.value))
E       AssertionError: Expected UnsupportedLocale error, got Locale «unsupported_locale» is not supported
E       assert False
E        +  where False = <built-in method startswith of str object at 0x7faa3abb3030>('UnsupportedLocale')
E        +    where <built-in method startswith of str object at 0x7faa3abb3030> = 'Locale «unsupported_locale» is not supported'.startswith
E        +      where 'Locale «unsupported_locale» is not supported' = str(UnsupportedLocale('unsupported_locale'))
E        +        where UnsupportedLocale('unsupported_locale') = <ExceptionInfo UnsupportedLocale('unsupported_locale') tblen=4>.value

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_academic_degree_0.py:16: AssertionError
_________________________ test_edge_case_no_parameters _________________________

    def test_edge_case_no_parameters():
>       with pytest.raises(TypeError):
E       Failed: DID NOT RAISE <class 'TypeError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_academic_degree_0.py:19: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_academic_degree_0.py::test_valid_case_with_locale
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_academic_degree_0.py::test_invalid_locale
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_academic_degree_0.py::test_edge_case_no_parameters
============================== 3 failed in 0.15s ===============================
"""