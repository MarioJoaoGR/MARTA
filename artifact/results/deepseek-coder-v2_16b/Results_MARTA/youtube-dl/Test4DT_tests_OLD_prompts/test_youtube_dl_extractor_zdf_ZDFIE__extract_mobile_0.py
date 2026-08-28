
import pytest
from unittest.mock import patch
from youtube_dl.extractor.zdf import ZDFIE
from youtube_dl.utils import ExtractorError

# Test for valid case scenario

# Test for edge case scenario where no formats are available
def test_edge_case():
    zdf_ie = ZDFIE()
    with patch('youtube_dl.extractor.zdf.ZDFIE._download_json', return_value={'document': {'titel': 'Edge Case Title', 'basename': 'edge123', 'formitaeten': [], 'teaserBild': {}}}):
        with pytest.raises(ExtractorError):
            zdf_ie._extract_mobile('edge123')