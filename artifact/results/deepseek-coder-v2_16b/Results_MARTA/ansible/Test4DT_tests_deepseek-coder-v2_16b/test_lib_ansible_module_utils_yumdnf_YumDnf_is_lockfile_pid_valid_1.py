
import pytest
from ansible.module_utils.yumdnf import YumDnf

def test_valid_case():
    module = {
        'allow_downgrade': True,
        'autoremove': False,
        'bugfix': True,
        'cacheonly': False,
        'conf_file': '/etc/yum.conf',
        'disable_excludes': 'all',
        'disable_gpg_check': True,
        'disable_plugin': False,
        'disablerepo': ['updates'],
        'download_only': False,
        'download_dir': '/var/cache/yum',
        'enable_plugin': True,
        'enablerepo': ['epel'],
        'exclude': ['kernel*'],
        'installroot': '/opt',
        'install_repoquery': True,
        'install_weak_deps': True,
        'list': True,
        'names': ['vim', 'git'],
        'releasever': '7',
        'security': False,
        'skip_broken': False,
        'state': 'present',
        'update_only': False,
        'update_cache': True,
        'validate_certs': True,
        'lock_timeout': 60
    }
    
    with pytest.raises(TypeError):
        yum_dnf = YumDnf(module=module)
