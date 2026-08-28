
import pytest
from youtube_dl.postprocessor.common import PostProcessor

def test_init_without_downloader():
    post_processor = PostProcessor()
    assert post_processor._downloader is None

def test_init_with_downloader():
    from youtube_dl import YoutubeDL
    downloader = YoutubeDL()
    post_processor = PostProcessor(downloader=downloader)
    assert post_processor._downloader == downloader

def test_set_downloader():
    post_processor = PostProcessor()
    from youtube_dl import YoutubeDL
    downloader = YoutubeDL()
    post_processor.set_downloader(downloader)
    assert post_processor._downloader == downloader
