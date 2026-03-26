
import os
import tempfile
import tarfile
import zipfile
from typing import Optional, Callable
from flutes.network import extract_google_drive_file_id, _download_from_google_drive
from unittest.mock import patch
import pytest

def download(url: str, save_dir: Optional[str] = None, filename: Optional[str] = None, extract: bool = False,
             progress: bool = False, bar_fn: Optional[Callable[[], object]] = None, **kwargs) -> str:
    """
    Download a file from the given URL. If the given file already exists in the save directory, download is skipped.
    
    Supported URL types include:
    - Any direct URL to files.
    - Google Drive shared file URLs in the form of ``https://drive.google.com/file/d/<file_id>/view``.

    Parameters:
        url (str): The URL from which to download the file.
        save_dir (Optional[str]): The directory where the downloaded file will be saved. If not provided, a temporary directory is used.
        filename (Optional[str]): The name of the downloaded file. If not specified, it defaults to the last segment of the URL after removing any query parameters like ``?raw=true`` if applicable.
        extract (bool): Whether to extract compressed files after downloading. Defaults to False. Note that only .tar.gz, .tar.bz2, .tar, and .zip files are supported for extraction.
        progress (bool): Whether to display a progress bar during download. Defaults to False. Google Drive URLs do not support size estimation in the progress bar due to their nature.
        bar_fn (Optional[Callable[[], object]]): A callable for creating a custom progress bar. Useful for overriding the default progress bar, especially when using specific libraries like `tqdm`.
        **kwargs: Additional keyword arguments passed to the initializer of `tqdm` for progress bar customization.

    Returns:
        str: The path to the downloaded file.
    """
    if save_dir is None:
        save_dir_str = tempfile.gettempdir()
    else:
        save_dir_str = save_dir
        os.makedirs(save_dir_str, exist_ok=True)

    if filename is None:
        if 'drive.google.com' in url:
            filename = extract_google_drive_file_id(url)
        else:
            filename = url.split('/')[-1]
            # If downloading from GitHub, remove suffix ?raw=true from local filename.
            filename = remove_suffix(filename, "?raw=true")

    if progress:
        if bar_fn is None:
            from tqdm import tqdm
            bar_fn = tqdm
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

@pytest.mark.parametrize("url, expected_error", [
    ("invalid_url", ValueError),
    (None, TypeError)
])
def test_download_invalid_input(url, expected_error):
    with pytest.raises(expected_error):
        download(url)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network_download_0_test_invalid_input
flutes/Test4DT_tests/test_flutes_network_download_0_test_invalid_input.py:7:0: E0611: No name 'extract_google_drive_file_id' in module 'flutes.network' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_network_download_0_test_invalid_input.py:44:23: E0602: Undefined variable 'remove_suffix' (undefined-variable)
flutes/Test4DT_tests/test_flutes_network_download_0_test_invalid_input.py:50:17: E0602: Undefined variable 'functools' (undefined-variable)
flutes/Test4DT_tests/test_flutes_network_download_0_test_invalid_input.py:59:23: E0602: Undefined variable '_download' (undefined-variable)
flutes/Test4DT_tests/test_flutes_network_download_0_test_invalid_input.py:69:16: E0602: Undefined variable 'log' (undefined-variable)


"""