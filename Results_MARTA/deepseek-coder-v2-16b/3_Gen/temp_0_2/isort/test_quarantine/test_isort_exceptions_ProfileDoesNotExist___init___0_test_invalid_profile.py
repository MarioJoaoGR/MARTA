
import pytest
from isort.exceptions import ProfileDoesNotExist, profiles

def set_profile(profile):
    if profile not in profiles:
        raise ProfileDoesNotExist(profile)

@pytest.mark.parametrize("invalid_profile, expected_message", [
    ("non_existent_profile", "Specified profile of non_existent_profile does not exist. Available profiles: existing_profile1,existing_profile2.")
])
def test_invalid_profile(invalid_profile, expected_message):
    with pytest.raises(ProfileDoesNotExist) as excinfo:
        set_profile(invalid_profile)
    assert str(excinfo.value) == expected_message

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 1 item

isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_invalid_profile.py F [100%]

=================================== FAILURES ===================================
_ test_invalid_profile[non_existent_profile-Specified profile of non_existent_profile does not exist. Available profiles: existing_profile1,existing_profile2.] _

invalid_profile = 'non_existent_profile'
expected_message = 'Specified profile of non_existent_profile does not exist. Available profiles: existing_profile1,existing_profile2.'

    @pytest.mark.parametrize("invalid_profile, expected_message", [
        ("non_existent_profile", "Specified profile of non_existent_profile does not exist. Available profiles: existing_profile1,existing_profile2.")
    ])
    def test_invalid_profile(invalid_profile, expected_message):
        with pytest.raises(ProfileDoesNotExist) as excinfo:
            set_profile(invalid_profile)
>       assert str(excinfo.value) == expected_message
E       AssertionError: assert 'Specified pr...ake,appnexus.' == 'Specified pr...ing_profile2.'
E         
E         Skipping 68 identical leading characters in diff, use -v to show
E         - profiles: existing_profile1,existing_profile2.
E         + profiles: black,django,pycharm,google,open_stack,plone,attrs,hug,wemake,appnexus.

isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_invalid_profile.py:15: AssertionError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0_test_invalid_profile.py::test_invalid_profile[non_existent_profile-Specified profile of non_existent_profile does not exist. Available profiles: existing_profile1,existing_profile2.]
============================== 1 failed in 0.13s ===============================
"""