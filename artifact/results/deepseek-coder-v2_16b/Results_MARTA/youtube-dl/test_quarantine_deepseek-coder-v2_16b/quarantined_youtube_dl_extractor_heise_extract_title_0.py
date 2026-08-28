
import pytest
from youtube_dl.extractor.heise import extract_title, NO_DEFAULT

def test_extract_title_with_default():
    webpage = '<html><head><meta name="fulltitle" content="Example Title"></head></html>'
    assert extract_title() == 'Example Title'

def test_extract_title_without_default():
    webpage = '<html><head></head><body><div class="videoplayerjw" data-title=""></div></body></html>'
    with pytest.raises(ValueError):
        extract_title()

def test_extract_title_with_custom_default():
    webpage = '<html><head></head><body><div class="videoplayerjw" data-title=""></div></body></html>'
    assert extract_title(default='Unknown') == 'Unknown'

def test_extract_title_from_h1_tag():
    webpage = '<html><head></head><body><h1 class="article_page_title">Article Title</h1></body></html>'
    assert extract_title() == 'Article Title'

def test_extract_title_with_no_tags():
    webpage = '<html><head></head><body><div class="videoplayerjw" data-title=""></div></body></html>'
    with pytest.raises(ValueError):
        extract_title()

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
_____ ERROR collecting test_youtube_dl_extractor_heise_extract_title_0.py ______
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_heise_extract_title_0.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_heise_extract_title_0.py:3: in <module>
    from youtube_dl.extractor.heise import extract_title, NO_DEFAULT
E   ImportError: cannot import name 'extract_title' from 'youtube_dl.extractor.heise' (/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/heise.py)
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_heise_extract_title_0.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.61s ===============================
"""