import pytest
import argparse
from sphinx.cmd.build import jobs_argument

def test_jobs_argument_auto():
    result = jobs_argument("auto")
    assert result > 0

def test_jobs_argument_positive_int():
    result = jobs_argument("123")
    assert result == 123

def test_jobs_argument_negative_int():
    with pytest.raises(argparse.ArgumentTypeError) as excinfo:
        jobs_argument('0')
    assert str(excinfo.value) == 'job number should be a positive number'

if __name__ == '__main__':
    test_jobs_argument_auto()
    test_jobs_argument_positive_int()
    test_jobs_argument_negative_int()