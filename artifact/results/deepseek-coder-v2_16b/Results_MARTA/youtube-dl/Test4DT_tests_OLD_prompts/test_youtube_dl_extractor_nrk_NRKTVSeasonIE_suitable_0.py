
import pytest
from unittest.mock import patch
from youtube_dl.extractor.nrk import NRKTVSeasonIE, NRKTVIE, NRKTVEpisodeIE, NRKRadioPodkastIE



def test_valid_tv_series():
    url = 'https://tv.nrk.no/serie/backstage/sesong/1'
    with patch('youtube_dl.extractor.nrk.NRKTVSeasonIE._real_extract', return_value={'id': 'backstage/1', 'title': 'Sesong 1'}):
        season_ie = NRKTVSeasonIE()
        assert season_ie.suitable(url) is True

def test_valid_radio_podcast():
    url = 'https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant'
    with patch('youtube_dl.extractor.nrk.NRKTVSeasonIE._real_extract', return_value={'id': 'hele_historien/diagnose-kverulant', 'title': 'Diagnose kverulant'}):
        season_ie = NRKTVSeasonIE()
        assert season_ie.suitable(url) is True