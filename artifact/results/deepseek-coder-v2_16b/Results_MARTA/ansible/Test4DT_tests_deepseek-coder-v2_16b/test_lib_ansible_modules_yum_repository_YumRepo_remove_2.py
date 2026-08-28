
import pytest
from ansible.modules.yum_repository import YumRepo
import os
import configparser

@pytest.fixture(scope="module")
def valid_repo():
    module = type('MockModule', (object,), {'params': {'repoid': 'test-repo', 'reposdir': '/tmp/repo'}})()
    repo = YumRepo(module)
    yield repo
    # Clean up if necessary
    if os.path.exists('/tmp/repo/test-repo.repo'):
        config = configparser.RawConfigParser()
        config.read('/tmp/repo/test-repo.repo')
        if config.has_section('test-repo'):
            config.remove_section('test-repo')
        with open('/tmp/repo/test-repo.repo', 'w') as f:
            config.write(f)


def test_invalid_inputs():
    module = type('MockModule', (object,), {'params': None})()
    with pytest.raises(TypeError):
        YumRepo(module)