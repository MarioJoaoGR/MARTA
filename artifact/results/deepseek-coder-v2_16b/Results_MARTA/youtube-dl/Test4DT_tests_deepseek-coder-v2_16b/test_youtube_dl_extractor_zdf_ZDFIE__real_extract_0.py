
import pytest
from youtube_dl.extractor.zdf import ZDFIE


def test_edge_case():
    zdf_ie = ZDFIE()
    url = None
    with pytest.raises(TypeError):
        metadata = zdf_ie._real_extract(url)
