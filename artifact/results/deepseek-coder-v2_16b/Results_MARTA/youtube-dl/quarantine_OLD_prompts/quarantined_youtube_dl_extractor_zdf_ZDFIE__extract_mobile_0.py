
import pytest
from unittest.mock import patch
from youtube_dl.extractor.zdf import ZDFIE

@pytest.fixture(scope="module")
def zdf_ie():
    return ZDFIE()

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_zdf_ZDFIE__extract_mobile_0.py F [100%]

=================================== FAILURES ===================================
_______________________________ test_valid_case ________________________________

mock_download = <MagicMock name='_download_json' id='139777355154960'>
zdf_ie = <youtube_dl.extractor.zdf.ZDFIE object at 0x7f20739a0670>

    @patch('youtube_dl.extractor.zdf.ZDFIE._download_json', return_value={
        'document': {
            'titel': 'Test Title',
            'basename': 'test123',
            'formitaeten': [
                {'url': 'https://example.com/video.mp4'},
                {'url': 'https://example.com/video2.mp4'}
            ],
            'teaserBild': {
                'thumbnail_key': {'url': 'https://example.com/thumbnail.jpg'}
            }
        }
    })
    def test_valid_case(mock_download, zdf_ie):
>       info_dict = zdf_ie._extract_mobile('test123')

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_zdf_ZDFIE__extract_mobile_0.py:24: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/zdf.py:257: in _extract_mobile
    self._sort_formats(formats)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:1446: in _sort_formats
    formats.sort(key=_formats_key)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

f = {'ext': 'mp4', 'format_id': 'http', 'format_note': None, 'language': None, ...}

    def _formats_key(f):
        # TODO remove the following workaround
        from ..utils import determine_ext
        if not f.get('ext') and 'url' in f:
            f['ext'] = determine_ext(f['url'])
    
        if isinstance(field_preference, (list, tuple)):
            return tuple(
                f.get(field)
                if f.get(field) is not None
                else ('' if field == 'format_id' else -1)
                for field in field_preference)
    
        preference = f.get('preference')
        if preference is None:
            preference = 0
            if f.get('ext') in ['f4f', 'f4m']:  # Not yet supported
                preference -= 0.5
    
        protocol = f.get('protocol') or determine_protocol(f)
        proto_preference = 0 if protocol in ['http', 'https'] else (-0.5 if protocol == 'rtsp' else -0.1)
    
        if f.get('vcodec') == 'none':  # audio only
            preference -= 50
            if self._downloader.params.get('prefer_free_formats'):
                ORDER = ['aac', 'mp3', 'm4a', 'webm', 'ogg', 'opus']
            else:
                ORDER = ['webm', 'opus', 'ogg', 'mp3', 'aac', 'm4a']
            ext_preference = 0
            try:
                audio_ext_preference = ORDER.index(f['ext'])
            except ValueError:
                audio_ext_preference = -1
        else:
            if f.get('acodec') == 'none':  # video only
                preference -= 40
>           if self._downloader.params.get('prefer_free_formats'):
E           AttributeError: 'NoneType' object has no attribute 'params'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:1418: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_zdf_ZDFIE__extract_mobile_0.py::test_valid_case
============================== 1 failed in 0.70s ===============================
"""