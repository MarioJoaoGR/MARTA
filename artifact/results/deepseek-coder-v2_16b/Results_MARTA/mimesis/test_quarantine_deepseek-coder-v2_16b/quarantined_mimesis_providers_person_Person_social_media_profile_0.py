
import pytest
from mimesis.providers.person import Person
from mimesis.enums import SocialNetwork


"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 2 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
________________________ test_valid_input_without_site _________________________

    def test_valid_input_without_site():
        person = Person(locale='en', seed=42)
        profile_url = person.social_media_profile()
        assert isinstance(profile_url, str), "Expected a string URL"
        supported_networks = [network for network in SocialNetwork]
        expected_prefixes = ['https://' + site.value for site in supported_networks]
>       assert profile_url in expected_prefixes, f"Expected URL to be one of the social networks, but got {profile_url}"
E       AssertionError: Expected URL to be one of the social networks, but got https://facebook.com/Huddlingly_1940
E       assert 'https://facebook.com/Huddlingly_1940' in ['https://facebook', 'https://twitter', 'https://instagram', 'https://vk']

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py:12: AssertionError
______________________ test_invalid_input_with_none_site _______________________

    def test_invalid_input_with_none_site():
        person = Person(locale='en', seed=42)
>       with pytest.raises(ValueError):
E       Failed: DID NOT RAISE <class 'ValueError'>

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py:16: Failed
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py::test_valid_input_without_site
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py::test_invalid_input_with_none_site
============================== 2 failed in 0.14s ===============================
"""