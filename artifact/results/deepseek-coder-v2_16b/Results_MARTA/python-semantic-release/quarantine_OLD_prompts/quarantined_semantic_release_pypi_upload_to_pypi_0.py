
import pytest
from unittest.mock import patch, MagicMock
from semantic_release.pypi import upload_to_pypi
import os

# Test 1: Basic Usage of upload_to_pypi function

# Test 2: Specifying Path to Upload Files

# Test 3: Setting Skip Existing to True

# Test 4: Specifying Glob Patterns

# Test 5: All Parameters Specified
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 5 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py F [ 20%]
FFFF                                                                     [100%]

=================================== FAILURES ===================================
__________________________ test_upload_to_pypi_basic ___________________________

    def test_upload_to_pypi_basic():
        with patch('semantic_release.pypi.os.environ', {'PYPI_TOKEN': 'valid-token'}):
>           result = upload_to_pypi()

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py:10: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py:70: in logged_func
    result = func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 'dist', skip_existing = False, glob_patterns = ['*']

    @LoggedFunction(logger)
    def upload_to_pypi(
        path: str = "dist", skip_existing: bool = False, glob_patterns: List[str] = None
    ):
        """Upload wheels to PyPI with Twine.
    
        Wheels must already be created and stored at the given path.
    
        Credentials are taken from either the environment variable
        ``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.
    
        :param path: Path to dist folder containing the files to upload.
        :param skip_existing: Continue uploading files if one already exists.
            (Only valid when uploading to PyPI. Other implementations may not support this.)
        :param glob_patterns: List of glob patterns to include in the upload (["*"] by default).
        """
        if not glob_patterns:
            glob_patterns = ["*"]
    
        # Attempt to get an API token from environment
        token = os.environ.get("PYPI_TOKEN")
        username = None
        password = None
        if not token:
            # Look for a username and password instead
            username = os.environ.get("PYPI_USERNAME")
            password = os.environ.get("PYPI_PASSWORD")
            home_dir = os.environ.get("HOME", "")
            if not (username or password) and (
                not home_dir or not os.path.isfile(os.path.join(home_dir, ".pypirc"))
            ):
                raise ImproperConfigurationError(
                    "Missing credentials for uploading to PyPI"
                )
        elif not token.startswith("pypi-"):
>           raise ImproperConfigurationError('PyPI token should begin with "pypi-"')
E           semantic_release.errors.ImproperConfigurationError: PyPI token should begin with "pypi-"

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/pypi.py:52: ImproperConfigurationError
________________________ test_upload_to_pypi_with_path _________________________

    def test_upload_to_pypi_with_path():
        with patch('semantic_release.pypi.os.environ', {'PYPI_TOKEN': 'valid-token'}):
>           result = upload_to_pypi(path="custom_dist")

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py:16: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py:70: in logged_func
    result = func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 'custom_dist', skip_existing = False, glob_patterns = ['*']

    @LoggedFunction(logger)
    def upload_to_pypi(
        path: str = "dist", skip_existing: bool = False, glob_patterns: List[str] = None
    ):
        """Upload wheels to PyPI with Twine.
    
        Wheels must already be created and stored at the given path.
    
        Credentials are taken from either the environment variable
        ``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.
    
        :param path: Path to dist folder containing the files to upload.
        :param skip_existing: Continue uploading files if one already exists.
            (Only valid when uploading to PyPI. Other implementations may not support this.)
        :param glob_patterns: List of glob patterns to include in the upload (["*"] by default).
        """
        if not glob_patterns:
            glob_patterns = ["*"]
    
        # Attempt to get an API token from environment
        token = os.environ.get("PYPI_TOKEN")
        username = None
        password = None
        if not token:
            # Look for a username and password instead
            username = os.environ.get("PYPI_USERNAME")
            password = os.environ.get("PYPI_PASSWORD")
            home_dir = os.environ.get("HOME", "")
            if not (username or password) and (
                not home_dir or not os.path.isfile(os.path.join(home_dir, ".pypirc"))
            ):
                raise ImproperConfigurationError(
                    "Missing credentials for uploading to PyPI"
                )
        elif not token.startswith("pypi-"):
>           raise ImproperConfigurationError('PyPI token should begin with "pypi-"')
E           semantic_release.errors.ImproperConfigurationError: PyPI token should begin with "pypi-"

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/pypi.py:52: ImproperConfigurationError
______________________ test_upload_to_pypi_skip_existing _______________________

    def test_upload_to_pypi_skip_existing():
        with patch('semantic_release.pypi.os.environ', {'PYPI_TOKEN': 'valid-token'}):
>           result = upload_to_pypi(skip_existing=True)

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py:22: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py:70: in logged_func
    result = func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 'dist', skip_existing = True, glob_patterns = ['*']

    @LoggedFunction(logger)
    def upload_to_pypi(
        path: str = "dist", skip_existing: bool = False, glob_patterns: List[str] = None
    ):
        """Upload wheels to PyPI with Twine.
    
        Wheels must already be created and stored at the given path.
    
        Credentials are taken from either the environment variable
        ``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.
    
        :param path: Path to dist folder containing the files to upload.
        :param skip_existing: Continue uploading files if one already exists.
            (Only valid when uploading to PyPI. Other implementations may not support this.)
        :param glob_patterns: List of glob patterns to include in the upload (["*"] by default).
        """
        if not glob_patterns:
            glob_patterns = ["*"]
    
        # Attempt to get an API token from environment
        token = os.environ.get("PYPI_TOKEN")
        username = None
        password = None
        if not token:
            # Look for a username and password instead
            username = os.environ.get("PYPI_USERNAME")
            password = os.environ.get("PYPI_PASSWORD")
            home_dir = os.environ.get("HOME", "")
            if not (username or password) and (
                not home_dir or not os.path.isfile(os.path.join(home_dir, ".pypirc"))
            ):
                raise ImproperConfigurationError(
                    "Missing credentials for uploading to PyPI"
                )
        elif not token.startswith("pypi-"):
>           raise ImproperConfigurationError('PyPI token should begin with "pypi-"')
E           semantic_release.errors.ImproperConfigurationError: PyPI token should begin with "pypi-"

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/pypi.py:52: ImproperConfigurationError
____________________ test_upload_to_pypi_with_glob_patterns ____________________

    def test_upload_to_pypi_with_glob_patterns():
        with patch('semantic_release.pypi.os.environ', {'PYPI_TOKEN': 'valid-token'}):
>           result = upload_to_pypi(glob_patterns=["*.whl", "*.tar.gz"])

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py:28: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py:70: in logged_func
    result = func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 'dist', skip_existing = False, glob_patterns = ['*.whl', '*.tar.gz']

    @LoggedFunction(logger)
    def upload_to_pypi(
        path: str = "dist", skip_existing: bool = False, glob_patterns: List[str] = None
    ):
        """Upload wheels to PyPI with Twine.
    
        Wheels must already be created and stored at the given path.
    
        Credentials are taken from either the environment variable
        ``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.
    
        :param path: Path to dist folder containing the files to upload.
        :param skip_existing: Continue uploading files if one already exists.
            (Only valid when uploading to PyPI. Other implementations may not support this.)
        :param glob_patterns: List of glob patterns to include in the upload (["*"] by default).
        """
        if not glob_patterns:
            glob_patterns = ["*"]
    
        # Attempt to get an API token from environment
        token = os.environ.get("PYPI_TOKEN")
        username = None
        password = None
        if not token:
            # Look for a username and password instead
            username = os.environ.get("PYPI_USERNAME")
            password = os.environ.get("PYPI_PASSWORD")
            home_dir = os.environ.get("HOME", "")
            if not (username or password) and (
                not home_dir or not os.path.isfile(os.path.join(home_dir, ".pypirc"))
            ):
                raise ImproperConfigurationError(
                    "Missing credentials for uploading to PyPI"
                )
        elif not token.startswith("pypi-"):
>           raise ImproperConfigurationError('PyPI token should begin with "pypi-"')
E           semantic_release.errors.ImproperConfigurationError: PyPI token should begin with "pypi-"

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/pypi.py:52: ImproperConfigurationError
______________________ test_upload_to_pypi_all_parameters ______________________

    def test_upload_to_pypi_all_parameters():
        with patch('semantic_release.pypi.os.environ', {'PYPI_TOKEN': 'valid-token'}):
>           result = upload_to_pypi(path="custom_dist", skip_existing=True, glob_patterns=["*.whl"])

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py:70: in logged_func
    result = func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

path = 'custom_dist', skip_existing = True, glob_patterns = ['*.whl']

    @LoggedFunction(logger)
    def upload_to_pypi(
        path: str = "dist", skip_existing: bool = False, glob_patterns: List[str] = None
    ):
        """Upload wheels to PyPI with Twine.
    
        Wheels must already be created and stored at the given path.
    
        Credentials are taken from either the environment variable
        ``PYPI_TOKEN``, or from ``PYPI_USERNAME`` and ``PYPI_PASSWORD``.
    
        :param path: Path to dist folder containing the files to upload.
        :param skip_existing: Continue uploading files if one already exists.
            (Only valid when uploading to PyPI. Other implementations may not support this.)
        :param glob_patterns: List of glob patterns to include in the upload (["*"] by default).
        """
        if not glob_patterns:
            glob_patterns = ["*"]
    
        # Attempt to get an API token from environment
        token = os.environ.get("PYPI_TOKEN")
        username = None
        password = None
        if not token:
            # Look for a username and password instead
            username = os.environ.get("PYPI_USERNAME")
            password = os.environ.get("PYPI_PASSWORD")
            home_dir = os.environ.get("HOME", "")
            if not (username or password) and (
                not home_dir or not os.path.isfile(os.path.join(home_dir, ".pypirc"))
            ):
                raise ImproperConfigurationError(
                    "Missing credentials for uploading to PyPI"
                )
        elif not token.startswith("pypi-"):
>           raise ImproperConfigurationError('PyPI token should begin with "pypi-"')
E           semantic_release.errors.ImproperConfigurationError: PyPI token should begin with "pypi-"

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/pypi.py:52: ImproperConfigurationError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py::test_upload_to_pypi_basic
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py::test_upload_to_pypi_with_path
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py::test_upload_to_pypi_skip_existing
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py::test_upload_to_pypi_with_glob_patterns
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_pypi_upload_to_pypi_0.py::test_upload_to_pypi_all_parameters
============================== 5 failed in 0.34s ===============================
"""