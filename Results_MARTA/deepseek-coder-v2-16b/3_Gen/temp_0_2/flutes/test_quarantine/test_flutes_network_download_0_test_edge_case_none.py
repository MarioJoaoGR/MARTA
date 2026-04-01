
import os
import tempfile
import tarfile
import zipfile
from typing import Optional, Callable
from flutes.network import extract_google_drive_file_id
from flutes.utils import remove_suffix, log  # Assuming utils module exists and has the required functions

def download(url: str, save_dir: Optional[str] = None, filename: Optional[str] = None, extract: bool = False, progress: bool = False, bar_fn: Optional[Callable[[], None]] = None, **kwargs) -> str:
    """
    Downloads a file from the given URL. Supports direct URLs to files and Google Drive shared file URLs. If the file already exists in the save directory, it skips downloading. The function can optionally extract compressed files during download. It supports progress bar visualization through optional arguments.

    Parameters:
        url (str): The URL from which to download the file.
        save_dir (Optional[str]): The directory to save the downloaded file. If None, a temporary directory is used.
        filename (Optional[str]): The name of the downloaded file. If None, the default filename from the URL is used.
        extract (bool): Whether to extract compressed files. Defaults to False.
        progress (bool): Whether to show download progress as a progress bar. Defaults to False.
        bar_fn (Optional[Callable[[], None]]): An optional callable that constructs a progress bar when called. Useful for customizing the progress bar.
        kwargs: Additional arguments to pass to `tqdm` initializer for initializing the progress bar.

    Returns:
        str: Path to the downloaded file.
    """
    if save_dir is None:
        save_dir = tempfile.gettempdir()
    else:
        os.makedirs(save_dir, exist_ok=True)

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

    filepath = os.path.join(save_dir, filename)
    if not os.path.exists(filepath):
        if 'drive.google.com' in url:
            filepath = _download_from_google_drive(url, filename, save_dir, bar_fn)
        else:
            filepath = _download(url, filename, save_dir, bar_fn)

        if extract:
            if tarfile.is_tarfile(filepath):
                with tarfile.open(filepath, 'r') as tfile:
                    tfile.extractall(save_dir)
            elif zipfile.is_zipfile(filepath):
                with zipfile.ZipFile(filepath) as zfile:
                    zfile.extractall(save_dir)
            else:
                log("Unknown compression type. Only .tar.gz, .tar.bz2, .tar, and .zip are supported", "warning")

    return filepath

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
************* Module Test4DT_tests.test_flutes_network_download_0_test_edge_case_none
flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py:7:0: E0611: No name 'extract_google_drive_file_id' in module 'flutes.network' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py:8:0: E0401: Unable to import 'flutes.utils' (import-error)
flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py:8:0: E0611: No name 'utils' in module 'flutes' (no-name-in-module)
flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py:43:17: E0602: Undefined variable 'functools' (undefined-variable)
flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py:50:23: E0602: Undefined variable '_download_from_google_drive' (undefined-variable)
flutes/Test4DT_tests/test_flutes_network_download_0_test_edge_case_none.py:52:23: E0602: Undefined variable '_download' (undefined-variable)


"""