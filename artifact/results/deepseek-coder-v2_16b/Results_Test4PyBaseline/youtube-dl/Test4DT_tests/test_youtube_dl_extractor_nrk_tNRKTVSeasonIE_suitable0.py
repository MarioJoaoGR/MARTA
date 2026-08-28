
import pytest
from youtube_dl.extractor.nrk import NRKTVSeasonIE

# Test cases for the suitable method
def test_suitable_valid_urls():
    nrk_season_ie = NRKTVSeasonIE()
    
    # Valid TV season URL
    assert nrk_season_ie.suitable('https://tv.nrk.no/serie/backstage/sesong/1') == True
    # Valid Radio podcast season URL
    assert nrk_season_ie.suitable('https://radio.nrk.no/podkast/hele_historien/sesong/diagnose-kverulant') == True
    
def test_suitable_invalid_urls():
    nrk_season_ie = NRKTVSeasonIE()
    
    # Valid TV URL but not for season extraction
    assert nrk_season_ie.suitable('https://tv.nrk.no/serie/backstage') == False
    # Valid Radio URL but not for season extraction
    assert nrk_season_ie.suitable('https://radio.nrk.no/podkast/hele_historien') == False
    
def test_suitable_urls_with_wrong_domain():
    nrk_season_ie = NRKTVSeasonIE()
    
    # URL with wrong domain
    assert nrk_season_ie.suitable('http://example.com/serie/backstage/sesong/1') == False
    # URL with correct domain but wrong path