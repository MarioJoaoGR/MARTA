
import pytest
from youtube_dl.extractor.nrk import NRKRadioPodkastIE

# Test for valid case

# Test for invalid case
def test_invalid_case():
    extractor = NRKRadioPodkastIE()
    url = 'https://radio.nrk.no/podkast/ulrikkes_univers/l_12345678-abcd-efgh-ijkl-mnopqrstuvwx'
    with pytest.raises(AssertionError):
        info = extractor._real_extract(url)