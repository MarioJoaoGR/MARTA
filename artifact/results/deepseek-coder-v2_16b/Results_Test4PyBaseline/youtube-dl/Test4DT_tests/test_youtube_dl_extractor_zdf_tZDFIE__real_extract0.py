
import pytest
from youtube_dl.extractor.zdf import ZDFIE

# Test cases for the _match_id method
def test_match_id():
    zdf_ie = ZDFIE()
    assert zdf_ie._match_id('https://www.zdf.de/politik/phoenix-sendungen/wohin-fuehrt-der-protest-in-der-pandemie-100.html') == 'wohin-fuehrt-der-protest-in-der-pandemie-100'