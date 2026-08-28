
import pytest
from unittest.mock import patch
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
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_______________________ test_valid_social_media_profile ________________________

    def test_valid_social_media_profile():
        with patch('mimesis.Person.__init__', return_value=None):
            person = Person(locale='en')
            site = SocialNetwork.FACEBOOK
>           result = person.social_media_profile(site)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py:11: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/person.py:289: in social_media_profile
    return url.format(self.username())
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.person.Person object at 0x7f8b1a7171f0>
template = None

    def username(self, template: Optional[str] = None) -> str:
        """Generate username by template.
    
        Supported template placeholders: (U, l, d)
    
        Supported separators: (-, ., _)
    
        Template must contain at least one "U" or "l" placeholder.
    
        If template is None one of the following templates is used:
        ('U_d', 'U.d', 'U-d', 'UU-d', 'UU.d', 'UU_d',
        'ld', 'l-d', 'Ud', 'l.d', 'l_d', 'default')
    
        :param template: Template.
        :return: Username.
        :raises ValueError: If template is not supported.
    
        :Example:
            Celloid1873
        """
        min_date = 1800
        max_date = 2070
        default_template = 'l.d'
    
        templates = ('U_d', 'U.d', 'U-d', 'UU-d', 'UU.d', 'UU_d',
                     'ld', 'l-d', 'Ud', 'l.d', 'l_d', 'default')
    
        if template is None:
>           template = self.random.choice(templates)
E           AttributeError: 'Person' object has no attribute 'random'

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/person.py:199: AttributeError
______________________ test_invalid_social_media_profile _______________________

    def test_invalid_social_media_profile():
        with patch('mimesis.Person.__init__', return_value=None):
            person = Person(locale='en')
            site = 'InvalidSocialNetwork'
            with pytest.raises(ValueError) as excinfo:
>               person.social_media_profile(site)

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py:20: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/person.py:286: in social_media_profile
    key = self._validate_enum(site, SocialNetwork)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.person.Person object at 0x7f8b1a364430>
item = 'InvalidSocialNetwork', enum = <enum 'SocialNetwork'>

    def _validate_enum(self, item: Any, enum: Any) -> Any:
        """Validate enum parameter of method in subclasses of BaseProvider.
    
        :param item: Item of enum object.
        :param enum: Enum object.
        :return: Value of item.
        :raises NonEnumerableError: if ``item`` not in ``enum``.
        """
        if item is None:
            result = get_random_item(enum, self.random)
        elif item and isinstance(item, enum):
            result = item
        else:
>           raise NonEnumerableError(enum)
E           mimesis.exceptions.NonEnumerableError: You should use one item of: «SocialNetwork.FACEBOOK, SocialNetwork.TWITTER, SocialNetwork.INSTAGRAM, SocialNetwork.VK» of the object mimesis.enums.SocialNetwork

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:64: NonEnumerableError
____________________ test_missing_site_social_media_profile ____________________

    def test_missing_site_social_media_profile():
        with patch('mimesis.Person.__init__', return_value=None):
            person = Person(locale='en')
            with pytest.raises(ValueError) as excinfo:
>               person.social_media_profile()

/opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py:27: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/person.py:286: in social_media_profile
    key = self._validate_enum(site, SocialNetwork)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <mimesis.providers.person.Person object at 0x7f8b1a523fd0>, item = None
enum = <enum 'SocialNetwork'>

    def _validate_enum(self, item: Any, enum: Any) -> Any:
        """Validate enum parameter of method in subclasses of BaseProvider.
    
        :param item: Item of enum object.
        :param enum: Enum object.
        :return: Value of item.
        :raises NonEnumerableError: if ``item`` not in ``enum``.
        """
        if item is None:
>           result = get_random_item(enum, self.random)
E           AttributeError: 'Person' object has no attribute 'random'

/opt/marta/baselines/codamosa/replication/test-apps/mimesis/mimesis/providers/base.py:60: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py::test_valid_social_media_profile
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py::test_invalid_social_media_profile
FAILED ../../../../../opt/marta/baselines/Results_MARTA/mimesis/Test4DT_tests_deepseek-coder-v2_16b/test_mimesis_providers_person_Person_social_media_profile_0.py::test_missing_site_social_media_profile
============================== 3 failed in 0.16s ===============================
"""