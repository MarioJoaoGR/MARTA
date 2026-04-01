
import os
import tempfile
import tarfile
import zipfile
from typing import Optional, Callable
from pathlib import Path
import functools
from flutes.network import download as _download
from flutes.network import extract_google_drive_file_id as _extract_google_drive_file_id
from flutes.network import remove_suffix as _remove_suffix
from flutes.network import download_from_google_drive as _download_from_google_drive
import logging

# Configure logging for the module
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

def download(url: str, save_dir: Optional[Path] = None, filename: Optional[str] = None, extract: bool = False,
             progress: bool = False, bar_fn: Optional[Callable[[], Callable]] = None, **kwargs) -> str:
    """
    Download a file from the given URL. If the given file already exists in the save directory, download is skipped.
    
    Supported URL types include any direct URL to files and Google Drive shared file URLs.

    Parameters:
        url (str): The URL from which to download the file.
        save_dir (Optional[Path], optional): The directory where the downloaded file will be saved. If not provided, a temporary directory is used. This parameter should be a string or Path-like object representing the directory path.
        filename (Optional[str], optional): The name of the downloaded file. If not provided, the default filename from the URL is used. This parameter should be a string representing the desired filename.
        extract (bool, optional): Whether to extract compressed files after downloading. Defaults to False.
        progress (bool, optional): Whether to show download progress as a progress bar. Defaults to False. Note that for Google Drive URLs, file size estimates during downloading are not available.
        bar_fn (Optional[Callable[[], Callable]], optional): An optional callable that constructs a progress bar when called. This is useful when you want to override the default progress bar. The function should accept no arguments and return an object with `update` and optionally `close` methods to track the download progress.
        **kwargs: Additional keyword arguments are passed to the initializer of `tqdm <https://tqdm.github.io/>`_ for customizing the progress bar, if used.

    Returns:
        str: The path to the downloaded file.

    Examples:
        To download a file from a direct URL and save it in the current working directory without extracting or showing progress:
        
        >>> download("http://example.com/file", save_dir='.', filename=None, extract=False, progress=False)
        
        To download a file from Google Drive and automatically extract it to the specified directory with a custom progress bar:
        
        >>> def custom_bar():
        ...     return tqdm(total=100, desc="Downloading")
        ... 
        >>> download("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsTuVwXyZ0/view", save_dir='downloads', filename=None, extract=True, progress=True, bar_fn=custom_bar)
        
    Notes:
        - The function supports downloading files from direct URLs and Google Drive shared links.
        - If `save_dir` is not provided, a temporary directory will be used, and it is the user's responsibility to remove the file after use.
        - For Google Drive URLs, if `progress` is set to True, a custom progress bar can be provided using the `bar_fn` parameter. If no specific bar function is provided, a default progress bar from `tqdm` will be used.
    """
    if save_dir is None:
        save_dir_str = tempfile.gettempdir()
    else:
        save_dir_str = str(save_dir)
        Path(save_dir_str).mkdir(parents=True, exist_ok=True)

    if filename is None:
        if 'drive.google.com' in url:
            filename = _extract_google_drive_file_id(url)
        else:
            filename = url.split('/')[-1]
            # If downloading from GitHub, remove suffix ?raw=true from local filename.
            filename = _remove_suffix(filename, "?raw=true")

    if progress:
        if bar_fn is None:
            from tqdm import tqdm
            bar_fn = lambda: tqdm(total=100, desc="Downloading", **kwargs)
        else:
            bar_fn = functools.partial(bar_fn, **kwargs)
    else:
        bar_fn = None

    filepath = os.path.join(save_dir_str, filename)
    if not os.path.exists(filepath):
        if 'drive.google.com' in url:
            filepath = _download_from_google_drive(url, filename, save_dir_str, bar_fn)
        else:
            filepath = _download(url, filename, save_dir_str, bar_fn)

        if extract:
            if tarfile.is_tarfile(filepath):
                with tarfile.open(filepath, 'r') as tfile:
                    tfile.extractall(save_dir_str)
            elif zipfile.is_zipfile(filepath):
                with zipfile.ZipFile(filepath) as zfile:
                    zfile.extractall(save_dir_str)
            else:
                log("Unknown compression type. Only .tar.gz, .tar.bz2, .tar, and .zip are supported", "warning")

    return filepath

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network_download_1_test_invalid_url
flutes/Test4DT_tests/test_flutes_network_download_1_test_invalid_url.py:10:0: E0611: No name 'extract_google_drive_file_id' in module 'flutes.network' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_network_download_1_test_invalid_url.py:12:0: E0611: No name 'download_from_google_drive' in module 'flutes.network' (no-name-in-module)


"""