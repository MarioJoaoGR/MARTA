
import pytest
from isort.exceptions import ProfileDoesNotExist

# Assuming 'profiles' is a list containing available profiles
profiles = ['default', 'user1', 'admin']

def set_profile(profile_name):
    if profile_name not in profiles:
        raise ProfileDoesNotExist(profile_name)
    print(f"Profile {profile_name} has been set.")

# Test cases for the ProfileDoesNotExist exception
def test_set_profile_with_non_existent_profile():
    with pytest.raises(ProfileDoesNotExist) as exc_info:
        set_profile("non_existent_profile")
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/isort
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 2 items

isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0.py F [ 50%]
F                                                                        [100%]

=================================== FAILURES ===================================
__________________ test_set_profile_with_non_existent_profile __________________

    def test_set_profile_with_non_existent_profile():
        with pytest.raises(ProfileDoesNotExist) as exc_info:
            set_profile("non_existent_profile")
>       assert str(exc_info.value) == "Specified profile of non_existent_profile does not exist. Available profiles: default,user1,admin."
E       AssertionError: assert 'Specified pr...ake,appnexus.' == 'Specified pr...,user1,admin.'
E         
E         Skipping 68 identical leading characters in diff, use -v to show
E         - profiles: default,user1,admin.
E         + profiles: black,django,pycharm,google,open_stack,plone,attrs,hug,wemake,appnexus.

isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0.py:17: AssertionError
____________________ test_set_profile_with_existing_profile ____________________

    def test_set_profile_with_existing_profile():
>       with pytest.raises(ProfileDoesNotExist):
E       Failed: DID NOT RAISE <class 'isort.exceptions.ProfileDoesNotExist'>

isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0.py:20: Failed
----------------------------- Captured stdout call -----------------------------
Profile default has been set.
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
=========================== short test summary info ============================
FAILED isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0.py::test_set_profile_with_non_existent_profile
FAILED isort/Test4DT_tests/test_isort_exceptions_ProfileDoesNotExist___init___0.py::test_set_profile_with_existing_profile
============================== 2 failed in 0.11s ===============================
"""