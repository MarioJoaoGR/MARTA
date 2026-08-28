
import pytest
from youtube_dl.extractor import nrk as NRKIE

# Create an instance of NRKTVIE for testing
@pytest.fixture(scope="module")
def extractor():
    return NRKIE.NRKTVIE()

# Test cases for _real_extract method
@pytest.mark.parametrize("url, expected", [
    ('https://tv.nrk.no/program/MDDP12000117', {'id': 'MDDP12000117', 'ext': 'mp4', 'title': 'Alarm Trolltunga', 'description': 'md5:46923a6e6510eefcce23d5ef2a58f2ce', 'duration': 2223.44, 'age_limit': 6, 'subtitles': {'nb-nor': [{'ext': 'vtt'}], 'nb-ttv': [{'ext': 'vtt'}]}}),
    ('https://tv.nrk.no/serie/20-spoersmaal-tv/MUHH48000314/23-05-2014', {'id': 'MUHH48000314', 'ext': 'mp4', 'title': '20 spørsmål - 23. mai 2014', 'alt_title': '23. mai 2014', 'description': 'md5:bdea103bc35494c143c6a9acdd84887a', 'duration': 1741, 'series': '20 spørsmål', 'episode': '23. mai 2014', 'age_limit': 0}),
    ('https://tv.nrk.no/program/mdfp15000514', {'id': 'MDFP15000514', 'ext': 'mp4', 'title': 'Kunnskapskanalen - Grunnlovsjubiléet - Stor ståhei for ingenting', 'description': 'md5:89290c5ccde1b3a24bb8050ab67fe1db', 'duration': 4605.08, 'series': 'Kunnskapskanalen', 'episode': 'Grunnlovsjubiléet - Stor ståhei for ingenting', 'age_limit': 0}),
    ('https://tv.nrk.no/serie/tour-de-ski/MSPO40010515/06-01-2015#del=2', {'id': 'MSPO40010515', 'ext': 'mp4', 'title': 'Sprint fri teknikk, kvinner og menn 06.01.2015', 'description': 'md5:c03aba1e917561eface5214020551b7a', 'age_limit': 0}),
    ('https://tv.nrk.no/serie/anno/KMTE50001317/sesong-3/episode-13', {'id': 'KMTE50001317', 'ext': 'mp4', 'title': 'Anno - 13. episode', 'description': 'md5:11d9613661a8dbe6f9bef54e3a4cbbfa', 'duration': 2340, 'series': 'Anno', 'episode': '13. episode', 'season_number': 3, 'episode_number': 13, 'age_limit': 0}),
    ('https://tv.nrk.no/serie/nytt-paa-nytt/MUHH46000317/27-01-2017', {'id': 'MUHH46000317', 'ext': 'mp4', 'title': 'Nytt på Nytt 27.01.2017', 'description': 'md5:5358d6388fba0ea6f0b6d11c48b9eb4b', 'duration': 1796, 'series': 'Nytt på nytt', 'episode': '27.01.2017', 'age_limit': 0}),
    ('https://radio.nrk.no/serie/dagsnytt/NPUB21019315/12-07-2015#', {'only_matching': True}),
    ('https://tv.nrk.no/serie/lindmo/2018/MUHU11006318/avspiller', {'only_matching': True}),
    ('https://radio.nrk.no/serie/dagsnytt/sesong/201507/NPUB21019315', {'only_matching': True})
])
def test_real_extract(extractor, url, expected):
    info_dict = extractor._real_extract(url)
    assert 'id' in info_dict, "Expected 'id' field not found"