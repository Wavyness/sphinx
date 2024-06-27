from sphinx._cli.util.colour import terminal_supports_colour
from unittest.mock import patch
import os

def test_no_colour():
    os.environ['NO_COLOUR'] = '1'
    result = terminal_supports_colour()
    del os.environ['NO_COLOUR']
    assert result == False

def test_force_colour():
    os.environ['FORCE_COLOUR'] = '1'
    result = terminal_supports_colour()
    del os.environ['FORCE_COLOUR']
    assert result == True

def test_standard():
    with patch('sys.stdout.isatty', return_value=False):
        result = terminal_supports_colour()
    assert result == False

def test_value_error():
    with patch('sys.stdout.isatty', side_effect=ValueError("I/O operation on closed file")):
        result = terminal_supports_colour()
    assert result == False

if __name__ == '__main__':
    test_no_colour()
    test_force_colour()
    test_standard()
    test_value_error()