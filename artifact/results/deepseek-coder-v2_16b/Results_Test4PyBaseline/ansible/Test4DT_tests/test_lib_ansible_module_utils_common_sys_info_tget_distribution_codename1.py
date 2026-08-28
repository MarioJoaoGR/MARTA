
import pytest
import platform
import distro

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
def test_get_distribution_codename_linux():
    # Mock platform.system to always return 'Linux'
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(platform, 'system', lambda: 'Linux')
        
        # Mock distro.os_release_info to return a dictionary with version_codename
        with pytest.MonkeyPatch.context() as mp2:
            mp2.setattr(distro, 'os_release_info', lambda: {'version_codename': 'xenial'})
            
            assert get_distribution_codename() == 'xenial'

def test_get_distribution_codename_not_linux():
    # Mock platform.system to always return a non-Linux value
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(platform, 'system', lambda: 'Windows')
        
        assert get_distribution_codename() is None

def test_get_distribution_codename_ubuntu():
    # Mock distro.id to always return 'ubuntu'
    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(distro, 'id', lambda: 'ubuntu')
        
        # Mock distro.lsb_release_info to return a dictionary with codename
        with pytest.MonkeyPatch.context() as mp2:
            mp2.setattr(distro, 'lsb_release_info', lambda: {'codename': 'xenial'})
            