
import os
import tempfile
import tarfile
import zipfile
from typing import Optional, Callable
from pathlib import Path
from flutes.utils import remove_suffix  # Assuming utils is in the same module as network
from flutes.network import _extract_google_drive_file_id, _download_from_google_drive, _download
import functools
import logging

# Configure logging for tests
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('test')

def download(url: str, save_dir: Optional[PathType] = None, filename: Optional[str] = None, extract: bool = False,
             progress: bool = False, bar_fn: Optional[BarFn] = None, **kwargs) -> str:
    """
    Download a file from the given URL. If the given file already exists in the save directory, download is skipped.
    
    Supported URL types include:
    - Any direct URL to files.
    - Google Drive shared file URLs in the form of ``https://drive.google.com/file/d/<file_id>/view``.

    Parameters:
        url (str): The URL from which to download the file.
        save_dir (Optional[PathType]): The directory where the downloaded file will be saved. If not provided, a temporary directory is used.
        filename (Optional[str]): The name of the downloaded file. If not specified, it defaults to the last segment of the URL after removing any query parameters like ``?raw=true`` if applicable.
        extract (bool): Whether to extract compressed files after downloading. Defaults to False. Note that only .tar.gz, .tar.bz2, .tar, and .zip files are supported for extraction.
        progress (bool): Whether to display a progress bar during download. Defaults to False. Google Drive URLs do not support size estimation in the progress bar due to their nature.
        bar_fn (Optional[BarFn]): A callable for creating a custom progress bar. Useful for overriding the default progress bar, especially when using specific libraries like `tqdm`.
        **kwargs: Additional keyword arguments passed to the initializer of `tqdm` for progress bar customization.

    Returns:
        str: The path to the downloaded file.

    Examples:
        >>> download("http://example.com/file", save_dir="downloads")  # Downloads a file from example.com and saves it in the "downloads" directory.
        >>> download("https://drive.google.com/file/d/1aBcD2eF3gHiJkLmNoPqRsT/view", extract=True)  # Downloads a Google Drive file and extracts it automatically.
        >>> from tqdm import tqdm
        >>> download("http://example.com/file", progress=True, bar_fn=tqdm)  # Displays a progress bar while downloading the file using tqdm.

    Notes:
        - The function supports direct URLs to files and Google Drive shared links.
        - If `save_dir` is not provided, a temporary directory will be used for saving the file.
        - If `filename` is not specified, the default filename from the URL is used after removing any query parameters like ``?raw=true`` if applicable.
        - The function can optionally extract compressed files based on their extension (only .tar.gz, .tar.bz2, .tar, and .zip are supported).
        - Progress updates during download can be enabled with the `progress` parameter, using a customizable progress bar via the `bar_fn` parameter.
    """
    if save_dir is None:
        save_dir_str = tempfile.gettempdir()
    else:
        save_dir_str = str(save_dir)
        os.makedirs(save_dir_str, exist_ok=True)

    if filename is None:
        if 'drive.google.com' in url:
            filename = _extract_google_drive_file_id(url)
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

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network_download_0_test_valid_input
flutes/Test4DT_tests/test_flutes_network_download_0_test_valid_input.py:8:0: E0401: Unable to import 'flutes.utils' (import-error)
flutes/Test4DT_tests/test_flutes_network_download_0_test_valid_input.py:8:0: E0611: No name 'utils' in module 'flutes' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_network_download_0_test_valid_input.py:17:42: E0602: Undefined variable 'PathType' (undefined-variable)
flutes/Test4DT_tests/test_flutes_network_download_0_test_valid_input.py:18:54: E0602: Undefined variable 'BarFn' (undefined-variable)


"""