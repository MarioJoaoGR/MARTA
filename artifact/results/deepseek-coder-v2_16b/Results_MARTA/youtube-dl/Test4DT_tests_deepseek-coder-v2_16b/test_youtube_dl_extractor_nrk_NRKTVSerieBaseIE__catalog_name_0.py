
import pytest
from youtube_dl.extractor.nrk import NRKTVSerieBaseIE

def test_valid_podcast():
    nrk = NRKTVSerieBaseIE()
    assert nrk._catalog_name('podcast') == 'podcast'

def test_valid_podkast():
    nrk = NRKTVSerieBaseIE()
    assert nrk._catalog_name('podkast') == 'podcast'

def test_invalid_input():
    nrk = NRKTVSerieBaseIE()
    assert nrk._catalog_name('series') == 'series'
