
import pytest
from ansible.playbook.included_file import IncludedFile

# Test case for initialization without role association
@pytest.fixture
def included_file():
    return IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")

# Test case for initialization with role association
@pytest.fixture
def included_file_with_role():
    return IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy", is_role=True)

# Test case for initialization with a different task but same filename, args, and vars
@pytest.fixture
def included_file_same_content():
    return IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="other_task")

# Test case for initialization with a different filename but same args and vars
@pytest.fixture
def included_file_different_filename():
    return IncludedFile(filename="other_config.yml", args={"arg1": "value1"}, vars={"var1": "value1"}, task="deploy")

# Test case for initialization with a different args but same filename and vars
@pytest.fixture
def included_file_different_args():
    return IncludedFile(filename="config.yml", args={"arg2": "value2"}, vars={"var1": "value1"}, task="deploy")

# Test case for initialization with a different vars but same filename and args
@pytest.fixture
def included_file_different_vars():
    return IncludedFile(filename="config.yml", args={"arg1": "value1"}, vars={"var2": "value2"}, task="deploy")

# Test case for initialization with a different task, filename, args, and vars
@pytest.fixture
def included_file_different_all():
    return IncludedFile(filename="other_config.yml", args={"arg2": "value2"}, vars={"var2": "value2"}, task="other_task")

# Test case for equality check between two IncludedFile instances with the same content but different initialization
def test_equality_same_content(included_file, included_file_same_content):
    assert (included_file._filename == included_file_same_content._filename and
            included_file._args == included_file_same_content._args and
            included_file._vars == included_file_same_content._vars)

# Test case for inequality due to different filename
def test_inequality_different_filename(included_file, included_file_different_filename):
    assert (included_file._filename != included_file_different_filename._filename or
            included_file._args != included_file_different_filename._args or
            included_file._vars != included_file_different_filename._vars)

# Test case for inequality due to different args
def test_inequality_different_args(included_file, included_file_different_args):
    assert (included_file._args != included_file_different_args._args or
            included_file._vars != included_file_different_args._vars)

# Test case for inequality due to different vars
def test_inequality_different_vars(included_file, included_file_different_vars):
    assert (included_file._vars != included_file_different_vars._vars or
            included_file._args != included_file_different_vars._args)

# Test case for inequality due to different task
def test_inequality_different_task(included_file, included_file_same_content):
    assert (included_file._task != included_file_same_content._task or
            included_file._filename != included_file_same_content._filename or
            included_file._args != included_file_same_content._args or
            included_file._vars != included_file_same_content._vars)

# Test case for inequality due to different role association
def test_inequality_different_role(included_file, included_file_with_role):
    assert (included_file._is_role != included_file_with_role._is_role or
            included_file._task != included_file_with_role._task or
            included_file._filename != included_file_with_role._filename or
            included_file._args != included_file_with_role._args or
            included_file._vars != included_file_with_role._vars)
