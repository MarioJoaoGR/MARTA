
import pytest
from youtube_dl.postprocessor.metadatafromtitle import MetadataFromTitlePP

# Test successful extraction of metadata from title

# Test failed extraction due to invalid title format

# Test empty input results in KeyError
def test_empty_input():
    pp = MetadataFromTitlePP(None, '%(title)s - %(artist)s')  # Assuming downloader is None for this test
    info = {}
    
    with pytest.raises(KeyError):
        pp.run(info)