
import pytest
from unittest.mock import patch
from youtube_dl.extractor.nrk import NRKTVEpisodesIE


def test_edge_case():
    nrk_ie = NRKTVEpisodesIE()
    url = ''
    with pytest.raises(AttributeError):
        info_dict = nrk_ie.extract_info(url)