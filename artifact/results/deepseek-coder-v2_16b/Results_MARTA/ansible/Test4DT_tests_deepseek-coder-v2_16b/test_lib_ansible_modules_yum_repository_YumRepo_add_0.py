
import pytest
from ansible.modules.yum_repository import YumRepo
import configparser
import os

@pytest.fixture(scope="module")
def valid_repo():
    module = type('AnsibleModule', (object,), {'params': {}})
    repo = YumRepo(module)
    return repo

@pytest.mark.parametrize("param", [None, [], {}])
def test_edge_cases(valid_repo, param):
    valid_repo.params[next(iter(YumRepo.allowed_params))] = param
    with pytest.raises(SystemExit) as e:
        valid_repo.add()
    assert "Parameter 'baseurl', 'metalink' or 'mirrorlist' is required for adding a new repo." in str(e.value)

@pytest.mark.parametrize("invalid_param", ["invalid_value", 123, True])
def test_invalid_inputs(valid_repo, invalid_param):
    valid_repo.params[next(iter(YumRepo.allowed_params))] = invalid_param
    with pytest.raises(SystemExit) as e:
        valid_repo.add()
    assert "Parameter 'baseurl', 'metalink' or 'mirrorlist' is required for adding a new repo." in str(e.value)

def test_valid_inputs(valid_repo):
    valid_repo.params['repoid'] = 'test_repo'
    valid_repo.params['baseurl'] = 'http://example.com/repo'
    valid_repo.add()
    assert valid_repo.repofile.has_section('test_repo')
    assert valid_repo.repofile.get('test_repo', 'baseurl') == 'http://example.com/repo'
