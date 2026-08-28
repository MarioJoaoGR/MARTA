
import pytest
from ansible.playbook.role.requirement import RoleRequirement
from subprocess import Popen, PIPE
import os

def run_scm_cmd(cmd, tempdir):
    try:
        popen = Popen(cmd, cwd=tempdir, stdout=PIPE, stderr=PIPE)
        stdout, stderr = popen.communicate()
        if popen.returncode != 0:
            raise Exception(f"Command failed with return code {popen.returncode}: {stderr.decode('utf-8')}")
        return stdout.decode('utf-8'), stderr.decode('utf-8')
    except Exception as e:
        raise Exception(f"Error running command {cmd}: {str(e)}")

@pytest.fixture
def role_requirement():
    return RoleRequirement()


def test_invalid_inputs_error_handling():
    src = 'https://github.com/example/repo.git'
    with pytest.raises(Exception):
        role = RoleRequirement().scm_archive_role(src, scm='unsupported')