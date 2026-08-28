
import pytest
import platform
import distro
from unittest.mock import patch

def get_distribution_codename():
    '''
    Return the code name for this Linux Distribution

    :rtype: NativeString or None
    :returns: A string representation of the distribution's codename or None if not a Linux distro
    '''
    codename = None
    if platform.system() == 'Linux':
        # Until this gets merged and we update our bundled copy of distro:
        # https://github.com/nir0s/distro/pull/230
        # Fixes Fedora 28+ not having a code name and Ubuntu Xenial Xerus needing to be "xenial"
        os_release_info = distro.os_release_info()
        codename = os_release_info.get('version_codename')

        if codename is None:
            codename = os_release_info.get('ubuntu_codename')

        if codename is None and distro.id() == 'ubuntu':
            lsb_release_info = distro.lsb_release_info()
            codename = lsb_release_info.get('codename')

        if codename is None:
            codename = distro.codename()
            if codename == u'':
                codename = None

    return codename

# Test cases for get_distribution_codename function

def test_get_distribution_codename_ubuntu():
    with patch('distro.os_release_info', return_value={'version_codename': 'xenial'}):
        assert get_distribution_codename() == 'xenial'

def test_get_distribution_codename_debian():
    with patch('distro.os_release_info', return_value={'version_codename': 'buster'}):
        assert get_distribution_codename() == 'buster'

def test_get_distribution_codename_fedora():
    with patch('distro.os_release_info', return_value={'version_codename': 'rawhide'}):
        assert get_distribution_codename() == 'rawhide'
