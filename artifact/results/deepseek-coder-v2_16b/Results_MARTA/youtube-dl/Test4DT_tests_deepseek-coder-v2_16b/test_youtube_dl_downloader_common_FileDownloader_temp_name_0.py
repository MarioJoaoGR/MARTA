
import os
from unittest.mock import MagicMock
import pytest
from youtube_dl.downloader.common import FileDownloader


def test_temp_name_nopart():
    ydl = MagicMock()
    params = {'nopart': True}
    downloader = FileDownloader(ydl, params)
    filename = "samplefile"
    temp_filename = downloader.temp_name(filename)
    assert temp_filename == "samplefile", f"Expected samplefile, but got {temp_filename}"

def test_temp_name_download_pipe():
    ydl = MagicMock()
    params = {}
    downloader = FileDownloader(ydl, params)
    filename = "-"
    temp_filename = downloader.temp_name(filename)
    assert temp_filename == "-", f"Expected '-', but got {temp_filename}"