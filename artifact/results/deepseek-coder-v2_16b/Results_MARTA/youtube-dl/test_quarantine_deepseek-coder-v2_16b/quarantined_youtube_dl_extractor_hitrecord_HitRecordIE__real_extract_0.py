
import pytest
from youtube_dl.extractor.hitrecord import HitRecordIE

@pytest.fixture(scope="module")
def extractor():
    return HitRecordIE()

@pytest.mark.parametrize("url, expected", [
    ('https://hitrecord.org/records/2954362', {
        'id': '2954362',
        'url': 'https://hitrecord.org/api/web/records/2954362',
        'title': 'A Very Different World (HITRECORD x ACLU)',
        'description': 'md5:e62defaffab5075a5277736bead95a3d',
        'duration': 139.327,
        'timestamp': 1471557582,
        'uploader': 'Zuzi.C12',
        'uploader_id': '362811',
        'view_count': int,
        'like_count': int,
        'comment_count': int,
        'tags': ['HITRECORD', 'A Very Different World', 'ACLU']
    })
])
def test_valid_case(extractor, url, expected):
    info_dict = extractor._real_extract(url)
    assert info_dict['id'] == expected['id']
    assert info_dict['url'] == expected['url']
    assert info_dict['title'] == expected['title']
    assert info_dict['description'] == expected['description']
    assert info_dict['duration'] == expected['duration']
    assert info_dict['timestamp'] == expected['timestamp']
    assert info_dict['uploader'] == expected['uploader']
    assert info_dict['uploader_id'] == expected['uploader_id']
    assert isinstance(info_dict['view_count'], int)
    assert isinstance(info_dict['like_count'], int)
    assert isinstance(info_dict['comment_count'], int)
    assert info_dict['tags'] == expected['tags']
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 1 item

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_hitrecord_HitRecordIE__real_extract_0.py F [100%]

=================================== FAILURES ===================================
_______ test_valid_case[https://hitrecord.org/records/2954362-expected0] _______

extractor = <youtube_dl.extractor.hitrecord.HitRecordIE object at 0x7ff4174f94b0>
url = 'https://hitrecord.org/records/2954362'
expected = {'comment_count': <class 'int'>, 'description': 'md5:e62defaffab5075a5277736bead95a3d', 'duration': 139.327, 'id': '2954362', ...}

    @pytest.mark.parametrize("url, expected", [
        ('https://hitrecord.org/records/2954362', {
            'id': '2954362',
            'url': 'https://hitrecord.org/api/web/records/2954362',
            'title': 'A Very Different World (HITRECORD x ACLU)',
            'description': 'md5:e62defaffab5075a5277736bead95a3d',
            'duration': 139.327,
            'timestamp': 1471557582,
            'uploader': 'Zuzi.C12',
            'uploader_id': '362811',
            'view_count': int,
            'like_count': int,
            'comment_count': int,
            'tags': ['HITRECORD', 'A Very Different World', 'ACLU']
        })
    ])
    def test_valid_case(extractor, url, expected):
>       info_dict = extractor._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_hitrecord_HitRecordIE__real_extract_0.py:26: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/hitrecord.py:38: in _real_extract
    video = self._download_json(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:895: in _download_json
    res = self._download_json_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:874: in _download_json_handle
    res = self._download_webpage_handle(
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:667: in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:611: in _request_webpage
    self.to_screen('%s: %s' % (video_id, note))
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <youtube_dl.extractor.hitrecord.HitRecordIE object at 0x7ff4174f94b0>
msg = '2954362: Downloading JSON metadata'

    def to_screen(self, msg):
        """Print msg to screen, prefixing it with '[ie_name]'"""
>       self._downloader.to_screen('[%s] %s' % (self.IE_NAME, msg))
E       AttributeError: 'NoneType' object has no attribute 'to_screen'

/opt/marta/baselines/codamosa/replication/test-apps/youtube-dl/youtube_dl/extractor/common.py:921: AttributeError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_hitrecord_HitRecordIE__real_extract_0.py::test_valid_case[https:/hitrecord.org/records/2954362-expected0]
============================== 1 failed in 0.64s ===============================
"""