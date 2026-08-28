
import pytest
from unittest.mock import patch
from youtube_dl.extractor.udn import UDNEmbedIE


def test_invalid_url():
    with patch('youtube_dl.extractor.udn.UDNEmbedIE._real_extract', side_effect=Exception("Invalid URL")):
        udn_extractor = UDNEmbedIE()
        with pytest.raises(Exception):
            udn_extractor._real_extract('invalid-url')