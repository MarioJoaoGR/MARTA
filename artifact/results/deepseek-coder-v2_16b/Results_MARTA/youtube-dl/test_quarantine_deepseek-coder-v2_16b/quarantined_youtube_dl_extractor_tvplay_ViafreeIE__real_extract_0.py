
import pytest
from youtube_dl.extractor import TVPlayIE
from urllib.parse import urlparse

class ViafreeIE(TVPlayIE):
    _VALID_URL = r'(?x)\n                    https?://\n                        (?:www\.)?\n                        viafree\.(?P<country>dk|no|se)\n                        /(?P<id>program(?:mer)?/(?:[^/]+/)+[^/?#&]+)\n                    '
    _TESTS = [{'url': 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1', 'info_dict': {'id': '757786', 'ext': 'mp4', 'title': 'Det beste vorspielet - Sesong 2 - Episode 1', 'description': 'md5:b632cb848331404ccacd8cd03e83b4c3', 'series': 'Det beste vorspielet', 'season_number': 2, 'duration': 1116, 'timestamp': 1471200600, 'upload_date': '20160814'}, 'params': {'skip_download': True}}]
    _GEO_BYPASS = False
    
    def suitable(cls, url):
        return False if TVPlayIE.suitable(url) else super(ViafreeIE, cls).suitable(url)
    
    def _real_extract(self, url):
        country, path = re.match(self._VALID_URL, url).groups()
        content = self._download_json(
            'https://viafree-content.mtg-api.com/viafree-content/v1/%s/path/%s' % (country, path), path)
        program = content['_embedded']['viafreeBlocks'][0]['_embedded']['program']
        guid = program['guid']
        meta = content['meta']
        title = meta['title']

        try:
            stream_href = self._download_json(
                program['_links']['streamLink']['href'], guid,
                headers=self.geo_verification_headers())['embedded']['prioritizedStreams'][0]['links']['stream']['href']
        except ExtractorError as e:
            if isinstance(e.cause, compat_HTTPError) and e.cause.code == 403:
                self.raise_geo_restricted(countries=[country])
            raise

        formats = self._extract_m3u8_formats(stream_href, guid, 'mp4')
        self._sort_formats(formats)
        episode = program.get('episode') or {}

        return {
            'id': guid,
            'title': title,
            'thumbnail': meta.get('image'),
            'description': meta.get('description'),
            'series': episode.get('seriesTitle'),
            'episode_number': int_or_none(episode.get('episodeNumber')),
            'season_number': int_or_none(episode.get('seasonNumber')),
            'duration': int_or_none(try_get(program, lambda x: x['video']['duration']['milliseconds']), 1000),
            'timestamp': parse_iso8601(try_get(program, lambda x: x['availability']['start'])),
            'formats': formats,
        }

# Test cases for valid case
@pytest.mark.parametrize("url, expected", [
    ('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1', {'id': '757786', 'ext': 'mp4', 'title': 'Det beste vorspielet - Sesong 2 - Episode 1', 'description': 'md5:b632cb848331404ccacd8cd03e83b4c3', 'series': 'Det beste vorspielet', 'season_number': 2, 'duration': 1116, 'timestamp': 1471200600, 'upload_date': '20160814'}),
])
def test_valid_case(url, expected):
    ie = ViafreeIE()
    info_dict = ie._real_extract(url)
    assert info_dict == expected

# Test case for edge case
@pytest.mark.parametrize("url", [
    'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1',
])
def test_edge_case(url):
    ie = ViafreeIE()
    with pytest.raises(ExtractorError):
        ie._real_extract(url)

# Test case for invalid case
@pytest.mark.parametrize("url", [
    'http://www.viafree.se/invalid-url',
])
def test_invalid_case(url):
    ie = ViafreeIE()
    with pytest.raises(ExtractorError):
        ie._real_extract(url)
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.py F [ 33%]
FF                                                                       [100%]

=================================== FAILURES ===================================
_ test_valid_case[http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1-expected0] _

url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'
expected = {'description': 'md5:b632cb848331404ccacd8cd03e83b4c3', 'duration': 1116, 'ext': 'mp4', 'id': '757786', ...}

    @pytest.mark.parametrize("url, expected", [
        ('http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1', {'id': '757786', 'ext': 'mp4', 'title': 'Det beste vorspielet - Sesong 2 - Episode 1', 'description': 'md5:b632cb848331404ccacd8cd03e83b4c3', 'series': 'Det beste vorspielet', 'season_number': 2, 'duration': 1116, 'timestamp': 1471200600, 'upload_date': '20160814'}),
    ])
    def test_valid_case(url, expected):
        ie = ViafreeIE()
>       info_dict = ie._real_extract(url)

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.py:55: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

self = <test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.ViafreeIE object at 0x7f030d43ae30>
url = 'http://www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1'

    def _real_extract(self, url):
>       country, path = re.match(self._VALID_URL, url).groups()
E       NameError: name 're' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.py:15: NameError
_ test_edge_case[http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1] _

url = 'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1'

    @pytest.mark.parametrize("url", [
        'http://www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1',
    ])
    def test_edge_case(url):
        ie = ViafreeIE()
>       with pytest.raises(ExtractorError):
E       NameError: name 'ExtractorError' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.py:64: NameError
_____________ test_invalid_case[http://www.viafree.se/invalid-url] _____________

url = 'http://www.viafree.se/invalid-url'

    @pytest.mark.parametrize("url", [
        'http://www.viafree.se/invalid-url',
    ])
    def test_invalid_case(url):
        ie = ViafreeIE()
>       with pytest.raises(ExtractorError):
E       NameError: name 'ExtractorError' is not defined

/opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.py:73: NameError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.py::test_valid_case[http:/www.viafree.no/programmer/underholdning/det-beste-vorspielet/sesong-2/episode-1-expected0]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.py::test_edge_case[http:/www.viafree.se/program/reality/sommaren-med-youtube-stjarnorna/sasong-1/avsnitt-1]
FAILED ../../../../../opt/marta/baselines/Results_MARTA/youtube-dl/Test4DT_tests_deepseek-coder-v2_16b/test_youtube_dl_extractor_tvplay_ViafreeIE__real_extract_0.py::test_invalid_case[http:/www.viafree.se/invalid-url]
============================== 3 failed in 0.56s ===============================
"""