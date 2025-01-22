import sys
import pytest
from unittest.mock import patch
from src.python_sample_module import dummy_function
from src.cli_argparse import cli_command


def test_mocking_function(mocker):
    # Mocking can patch any function within the codebase, as long you define the full dotted path.
    mocker.patch("src.python_sample_module.load_data", return_value=2)
    assert dummy_function() == 2, "Value should be mocked"


def test_cli_version(mocker):
    test_args = ['program_name_ignored_by_argparse', '--name', "J. Doe", '--age', '30']
    with patch('sys.argv', test_args):
        cli_command()

    mocker.patch('sys.argv', test_args)
    cli_command()
    # After the test is done, pytest mocker will automatically undo the patch
