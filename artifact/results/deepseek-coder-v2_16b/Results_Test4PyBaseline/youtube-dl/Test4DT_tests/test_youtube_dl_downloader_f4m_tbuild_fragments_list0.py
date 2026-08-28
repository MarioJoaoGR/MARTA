
import pytest
import itertools
from youtube_dl.downloader.f4m import build_fragments_list

# Test cases for build_fragments_list function

def test_build_fragments_list_non_live():
    boot_info = {
        'segments': [{'segment_run': [(1, 3), (2, 2)]}],
        'fragments': [{'fragments': [{'first': 100}]}],
        'live': False
    }
    expected_output = [(1, 100), (1, 101), (1, 102), (2, 103), (2, 104)]
    assert build_fragments_list(boot_info) == expected_output

def test_build_fragments_list_live():
    boot_info = {
        'segments': [{'segment_run': [(1, 3), (2, 2)]}],
        'fragments': [{'fragments': [{'first': 100}]}],
        'live': True
    }
    expected_output = [(1, 100), (1, 101), (1, 102), (2, 103), (2, 104)]