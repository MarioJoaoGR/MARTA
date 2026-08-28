
import pytest
from unittest.mock import MagicMock, patch
from youtube_dl.postprocessor.metadatafromtitle import MetadataFromTitlePP

# Test 1: Handling a Video Title with Placeholders
def test_handle_video_title_with_placeholders():
    downloader = MagicMock()
    info_dict = {'title': 'Song Title - Artist Name'}
    
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    result, updated_info = pp.run(info_dict)
    
    assert updated_info == {'title': 'Song Title', 'artist': 'Artist Name'}

# Test 2: Handling a Video Title Without Placeholders (Default Format)

# Test 3: Handling a Video Title Without Placeholders Using Default Regex

# Test 4: Handling a Video Title with Placeholders Using Default Regex
def test_handle_video_title_with_placeholders_default_regex():
    downloader = MagicMock()
    info_dict = {'title': 'Song Title - Artist Name'}
    
    pp = MetadataFromTitlePP(downloader, '%(title)s - %(artist)s')
    result, updated_info = pp.run(info_dict)
    
    assert updated_info == {'title': 'Song Title', 'artist': 'Artist Name'}