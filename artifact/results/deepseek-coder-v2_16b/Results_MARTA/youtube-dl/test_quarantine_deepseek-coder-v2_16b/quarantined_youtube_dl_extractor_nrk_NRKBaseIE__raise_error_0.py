
import pytest
from youtube_dl.extractor.nrk import NRKBaseIE
from youtube_dl.compat import try_get
from unittest.mock import patch

# Test 1: Raise error when program is geo-blocked
def test_raise_error_program_is_geo_blocked():
    nrk_ie = NRKBaseIE()
    with pytest.raises(ExtractorError) as e:
        nrk_ie._raise_error({'messageType': 'ProgramIsGeoBlocked'})
    assert str(e.value) == "NRK said: Programmet har gått ut"

# Test 2: Raise error when no program rights
def test_raise_error_no_program_rights():
    nrk_ie = NRKBaseIE()
    with pytest.raises(ExtractorError) as e:
        nrk_ie._raise_error({'messageType': 'NoProgramRights'})
    assert str(e.value) == "NRK said: Ikke tilgjengelig"

# Test 3: Raise error when program rights have expired
def test_raise_error_program_rights_has_expired():
    nrk_ie = NRKBaseIE()
    with pytest.raises(ExtractorError) as e:
        nrk_ie._raise_error({'messageType': 'ProgramRightsHasExpired'})
    assert str(e.value) == "NRK said: Programmet har gått ut"

# Test 4: Raise error when program rights are not ready
def test_raise_error_program_rights_are_not_ready():
    nrk_ie = NRKBaseIE()
    with pytest.raises(ExtractorError) as e:
        nrk_ie._raise_error({'messageType': 'ProgramRightsAreNotReady'})
    assert str(e.value) == "Du kan dessverre ikke se eller høre programmet"

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 0 items / 1 error

==================================== ERRORS ====================================
__ ERROR collecting test_youtube_dl_extractor_nrk_NRKBaseIE__raise_error_0.py __
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKBaseIE__raise_error_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKBaseIE__raise_error_0.py:4: in <module>
    from youtube_dl.compat import try_get
E   ImportError: cannot import name 'try_get' from 'youtube_dl.compat' (/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/compat.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_nrk_NRKBaseIE__raise_error_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.62s ===============================
"""