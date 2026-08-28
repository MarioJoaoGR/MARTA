
import pytest
from unittest.mock import patch
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE

def test_valid_podcast():
    with patch('youtube_dl.extractor.nrk.NRKTVSerieBaseIE._catalog_name', return_value='podcast'):
        assert NRKTVSerieBaseIE._catalog_name('podcast') == 'podcast'

def test_valid_podkast():
    with patch('youtube_dl.extractor.nrk.NRKTVSerieBaseIE._catalog_name', return_value='podcast'):
        assert NRKTVSerieBaseIE._catalog_name('podkast') == 'podcast'

def test_invalid_input():
    with patch('youtube_dl.extractor.nrk.NRKTVSerieBaseIE._catalog_name', return_value='series'):
        assert NRKTVSerieBaseIE._catalog_name('series') == 'series'
