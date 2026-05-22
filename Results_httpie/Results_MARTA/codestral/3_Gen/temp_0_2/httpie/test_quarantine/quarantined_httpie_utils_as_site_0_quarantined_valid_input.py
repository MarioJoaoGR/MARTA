
import sysconfig
from pathlib import Path
import unittest.mock as mock

def as_site(path: Path, **extra_vars) -> Path:
    """
    Generates a path to the site-packages directory for a given Python environment.

    This function constructs and returns the path to the site-packages directory of a specified Python environment using sysconfig. It allows additional variables to be passed through `extra_vars` for customization.

    Parameters:
        path (Path): The base installation path where the Python environment is located. This should be an instance of Path from the built-in 'pathlib' module.
        **extra_vars: Additional keyword arguments that can be used to override or specify additional configuration settings for sysconfig. These are passed as variables in the `vars` dictionary to sysconfig.get_path.

    Returns:
        Path: A path object representing the site-packages directory of the specified Python environment.
    """
    with mock.patch('sysconfig.get_path') as mock_get_path:
        mock_get_path.return_value = str(path / 'site-packages')
        site_packages_path = sysconfig.get_path(
            'purelib',
            vars={'base': str(path), **extra_vars}
        )
    return Path(site_packages_path)

"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.11.15, pytest-8.3.2, pluggy-1.6.0
rootdir: /projects/F202407648IACDCF2/mario/httpie
configfile: pytest.ini
plugins: anyio-4.12.1, json-report-1.5.0, metadata-3.1.1
collected 0 items

--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_codestral.json
============================ no tests ran in 0.11s =============================
"""