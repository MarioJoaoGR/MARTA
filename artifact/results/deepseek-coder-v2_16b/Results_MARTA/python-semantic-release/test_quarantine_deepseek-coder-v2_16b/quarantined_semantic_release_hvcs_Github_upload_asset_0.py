
import pytest
from semantic_release.hvcs import Github
import os
import mimetypes
from unittest.mock import patch, MagicMock

class TestGithubUploadAsset:
    @classmethod
    def setup_class(cls):
        cls.owner = 'user'
        cls.repo = 'repo-name'
        cls.release_id = 123456789
        cls.file_path = '/path/to/local/file'
    
    def test_upload_asset_with_custom_label(self):
        with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
            result = Github.upload_asset(owner=self.owner, repo=self.repo, release_id=self.release_id, file=self.file_path, label='release-assets')
            assert result is True
    
    def test_upload_asset_without_custom_label(self):
        with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
            result = Github.upload_asset(owner=self.owner, repo=self.repo, release_id=self.release_id, file=self.file_path)
            assert result is True
    
    def test_upload_asset_invalid_file(self):
        with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
            with pytest.raises(FileNotFoundError):
                Github.upload_asset(owner=self.owner, repo=self.repo, release_id=self.release_id, file='/nonexistent/file')
"""
[TEST4PY QUARANTINE REPORT]
Reason: Test failed assertions or crashed.
Error Log:
============================= test session starts ==============================
platform linux -- Python 3.10.20, pytest-8.3.2, pluggy-1.6.0
rootdir: /opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b
plugins: metadata-3.1.1, json-report-1.5.0, anyio-4.12.1
collected 3 items

../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_upload_asset_0.py F [ 33%]
F.                                                                       [100%]

=================================== FAILURES ===================================
__________ TestGithubUploadAsset.test_upload_asset_with_custom_label ___________

self = <test_semantic_release_hvcs_Github_upload_asset_0.TestGithubUploadAsset object at 0x7f74cf7b77f0>

    def test_upload_asset_with_custom_label(self):
        with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
>           result = Github.upload_asset(owner=self.owner, repo=self.repo, release_id=self.release_id, file=self.file_path, label='release-assets')

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_upload_asset_0.py:18: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py:70: in logged_func
    result = func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'semantic_release.hvcs.Github'>, owner = 'user', repo = 'repo-name'
release_id = 123456789, file = '/path/to/local/file', label = 'release-assets'

    @classmethod
    @LoggedFunction(logger)
    def upload_asset(
        cls, owner: str, repo: str, release_id: int, file: str, label: str = None
    ) -> bool:
        """Upload an asset to an existing release
    
        https://docs.github.com/rest/reference/repos#upload-a-release-asset
    
        :param owner: The owner namespace of the repository
        :param repo: The repository name
        :param release_id: ID of the release to upload to
        :param file: Path of the file to upload
        :param label: Custom label for this file
    
        :return: The status of the request
        """
        url = f"https://uploads.github.com/repos/{owner}/{repo}/releases/{release_id}/assets"
    
        content_type = mimetypes.guess_type(file, strict=False)[0]
        if not content_type:
            content_type = "application/octet-stream"
    
        try:
            response = Github.session().post(
                url,
                params={"name": os.path.basename(file), "label": label},
                headers={
                    "Content-Type": content_type,
                },
>               data=open(file, "rb").read(),
            )
E           FileNotFoundError: [Errno 2] No such file or directory: '/path/to/local/file'

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/hvcs.py:304: FileNotFoundError
_________ TestGithubUploadAsset.test_upload_asset_without_custom_label _________

self = <test_semantic_release_hvcs_Github_upload_asset_0.TestGithubUploadAsset object at 0x7f74cf7b7d30>

    def test_upload_asset_without_custom_label(self):
        with patch('semantic_release.hvcs.Github.session', return_value=MagicMock()):
>           result = Github.upload_asset(owner=self.owner, repo=self.repo, release_id=self.release_id, file=self.file_path)

/opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_upload_asset_0.py:23: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 
/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/helpers.py:70: in logged_func
    result = func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ 

cls = <class 'semantic_release.hvcs.Github'>, owner = 'user', repo = 'repo-name'
release_id = 123456789, file = '/path/to/local/file', label = None

    @classmethod
    @LoggedFunction(logger)
    def upload_asset(
        cls, owner: str, repo: str, release_id: int, file: str, label: str = None
    ) -> bool:
        """Upload an asset to an existing release
    
        https://docs.github.com/rest/reference/repos#upload-a-release-asset
    
        :param owner: The owner namespace of the repository
        :param repo: The repository name
        :param release_id: ID of the release to upload to
        :param file: Path of the file to upload
        :param label: Custom label for this file
    
        :return: The status of the request
        """
        url = f"https://uploads.github.com/repos/{owner}/{repo}/releases/{release_id}/assets"
    
        content_type = mimetypes.guess_type(file, strict=False)[0]
        if not content_type:
            content_type = "application/octet-stream"
    
        try:
            response = Github.session().post(
                url,
                params={"name": os.path.basename(file), "label": label},
                headers={
                    "Content-Type": content_type,
                },
>               data=open(file, "rb").read(),
            )
E           FileNotFoundError: [Errno 2] No such file or directory: '/path/to/local/file'

/opt/marta/baselines/codamosa/replication/test-apps/python-semantic-release/semantic_release/hvcs.py:304: FileNotFoundError
--------------------------------- JSON report ----------------------------------
report saved to: pytest_report_deepseek-coder-v2_16b.json
=========================== short test summary info ============================
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_upload_asset_0.py::TestGithubUploadAsset::test_upload_asset_with_custom_label
FAILED ../../../../../opt/marta/baselines/Results_MARTA/python-semantic-release/Test4DT_tests_deepseek-coder-v2_16b/test_semantic_release_hvcs_Github_upload_asset_0.py::TestGithubUploadAsset::test_upload_asset_without_custom_label
========================= 2 failed, 1 passed in 0.18s ==========================
"""