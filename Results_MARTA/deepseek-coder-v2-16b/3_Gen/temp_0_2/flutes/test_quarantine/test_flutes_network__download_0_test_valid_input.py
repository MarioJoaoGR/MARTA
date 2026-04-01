
import os
import urllib.request
from typing import Optional, Callable as BarFn

def _download(url: str, filename: str, path: str, bar_fn: Optional[BarFn] = None) -> str:
    """
    Downloads a file from the given URL and saves it to the specified directory with the provided filename.
    
    Parameters:
        url (str): The HTTP or HTTPS URL from which the file will be downloaded.
        filename (str): The name of the file to save the downloaded content under in the specified directory.
        path (str): The directory where the file will be saved.
        bar_fn (Optional[BarFn]): An optional function that takes no arguments and returns a progress bar object. This is used to track download progress if provided.
    
    Returns:
        str: The full local path where the file has been downloaded.
    
    Examples:
        To download a file from a URL without showing progress:
        >>> _download('http://example.com/file.zip', 'file.zip', '/path/to/save')
        
        To download a file with a custom progress bar function:
        >>> def my_progress_bar():
        ...     return CustomProgressBar()  # Assuming CustomProgressBar is defined elsewhere
        ...
        >>> _download('http://example.com/file.zip', 'file.zip', '/path/to/save', bar_fn=my_progress_bar)
    """
    if bar_fn is None:
        progress = _progress_hook = None
    else:
        progress = None
        prev_count = 0

        def _progress_hook(count, block_size, total_size):
            nonlocal progress, prev_count
            if progress is None:
                progress = bar_fn()
            if total_size != -1 and progress.total is None:
                progress.total = total_size
                progress.refresh()
            if count > prev_count:
                progress.update((count - prev_count) * block_size)
                prev_count = count

    filepath = os.path.join(path, filename)
    with urllib.request.urlopen(url) as response, open(filepath, 'wb') as out_file:
        total_size = int(response.info().get('Content-Length', -1))
        if progress is None:
            data = response.read()  # Read the entire content at once
            out_file.write(data)
        else:
            chunk_size = 8192
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                out_file.write(chunk)
                _progress_hook(out_file.tell(), chunk_size, total_size)
        if progress is not None:
            progress.close()
    return filepath

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/flutes
configfile: ../../../../dev/null
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report.json
============================ no tests ran in 0.04s =============================
"""