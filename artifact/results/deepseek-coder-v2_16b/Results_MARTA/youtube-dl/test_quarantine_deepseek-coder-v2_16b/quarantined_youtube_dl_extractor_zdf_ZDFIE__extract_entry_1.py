
import pytest
from youtube_dl.extractor.zdf import ZDFIE
from urllib.parse import urljoin
import re
from utils import try_get, int_or_none, unified_timestamp, merge_dicts, url_or_none

# Test fixture for ZDFIE class
@pytest.fixture(scope="module")
def zdf_ie():
    return ZDFIE()

# Test case to extract metadata from a valid video URL
def test_extract_valid_metadata(zdf_ie):
    url = 'https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html'
    player = {'apiToken': 'your_api_token'}
    content = {
        'title': 'Wohin führt der Protest in der Pandemie?',
        'mainVideoContent': {
            'http://zdf.de/rels/target': {
                'duration': 1691,
                'http://zdf.de/rels/streams/ptmd': None,
                'http://zdf.de/rels/streams/ptmd-template': '/api/video/{playerId}/playlist'
            }
        },
        'teaserImageRef': {'layouts': {'layout_key': 'https://example.com/image.jpg'}}
    }
    video_id = '210222_phx_nachgehakt_corona_protest'
    
    metadata = zdf_ie._extract_entry(url, player, content, video_id)
    
    assert metadata['title'] == 'Wohin führt der Protest in der Pandemie?'
    assert metadata['duration'] == 1691
    assert metadata['thumbnails'][0]['url'] == 'https://example.com/image.jpg'

# Test case to handle an invalid URL
def test_extract_invalid_url(zdf_ie):
    url = 'https://www.example.com/invalid-video-page'
    player = {'apiToken': 'your_api_token'}
    content = {}
    video_id = None
    
    with pytest.raises(KeyError):
        zdf_ie._extract_entry(url, player, content, video_id)

# Test case to extract metadata from another valid video URL
def test_extract_another_valid_metadata(zdf_ie):
    url = 'https://www.zdf.de/dokumentation/ab-18/10-wochen-sommer-102.html'
    player = {'apiToken': 'your_api_token'}
    content = {
        'title': 'Ab 18! - 10 Wochen Sommer',
        'mainVideoContent': {
            'http://zdf.de/rels/target': {
                'duration': 2660,
                'http://zdf.de/rels/streams/ptmd': None,
                'http://zdf.de/rels/streams/ptmd-template': '/api/video/{playerId}/playlist'
            }
        },
        'teaserImageRef': {'layouts': {'layout_key': 'https://example.com/image2.jpg'}}
    }
    video_id = '141007_ab18_10wochensommer_film'
    
    metadata = zdf_ie._extract_entry(url, player, content, video_id)
    
    assert metadata['title'] == 'Ab 18! - 10 Wochen Sommer'
    assert metadata['duration'] == 2660
    assert metadata['thumbnails'][0]['url'] == 'https://example.com/image2.jpg'

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
___ ERROR collecting test_youtube_dl_extractor_zdf_ZDFIE__extract_entry_1.py ___
ImportError while importing test module '/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_zdf_ZDFIE__extract_entry_1.py'.
Hint: make sure your test modules/packages have valid Python names.
Traceback:
/opt/conda/envs/test4py_env/lib/python3.10/importlib/__init__.py:126: in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_zdf_ZDFIE__extract_entry_1.py:6: in <module>
    from utils import try_get, int_or_none, unified_timestamp, merge_dicts, url_or_none
E   ModuleNotFoundError: No module named 'utils'
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
ERROR ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_zdf_ZDFIE__extract_entry_1.py
!!!!!!!!!!!!!!!!!!!! Interrupted: 1 error during collection !!!!!!!!!!!!!!!!!!!!
=============================== 1 error in 0.62s ===============================
"""