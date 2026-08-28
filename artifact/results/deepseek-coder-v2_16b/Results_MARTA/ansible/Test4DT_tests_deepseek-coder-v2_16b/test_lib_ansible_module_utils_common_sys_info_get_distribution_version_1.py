
import pytest
from unittest.mock import patch, MagicMock
import distro

def get_distribution_version():
    '''
    Get the version of the distribution the code is running on

    :rtype: NativeString or None
    :returns: A string representation of the version of the distribution. If it
    cannot determine the version, it returns an empty string. If this is not run on
    a Linux machine it returns None.
    '''
    version = None

    needs_best_version = frozenset((
        u'centos',
        u'debian',
    ))

    version = distro.version()
    distro_id = distro.id()

    if version is not None:
        if distro_id in needs_best_version:
            version_best = distro.version(best=True)

            # CentoOS maintainers believe only the major version is appropriate
            # but Ansible users desire minor version information, e.g., 7.5.
            # https://github.com/ansible/ansible/issues/50141#issuecomment-449452781
            if distro_id == u'centos':
                version = u'.'.join(version_best.split(u'.')[:2])

            # Debian does not include minor version in /etc/os-release.
            # Bug report filed upstream requesting this be added to /etc/os-release
            # https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=931197
            if distro_id == u'debian':
                version = version_best

    else:
        version = u''

    return version

# Test scenarios
def test_valid_case():
    with patch('distro.id', return_value='centos'):
        with patch('distro.version', return_value='7.8'):
            assert get_distribution_version() == '7.8'

def test_edge_case():
    with patch('distro.id', return_value=None):
        assert get_distribution_version() == ''

def test_error_case():
    with patch('sys.platform', new='linux2'):  # Mocking sys.platform to simulate Linux
        distro.__dict__.update({'id': MagicMock(return_value='unknown'), 'version': MagicMock(return_value='1.0')})
        assert get_distribution_version() is None
