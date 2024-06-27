from sphinx._cli.util.colour import colourise, enable_colour, disable_colour

def test_colourise_disabled_colour():
    disable_colour()
    result = colourise("red", "- test colourise disabled")
    assert result == "- test colourise disabled"

def test_colourise_enabled_colour():
    enable_colour()
    result = colourise("green", "- test colourise enabled")
    assert result.endswith('\x1b[39;49;00m')

if __name__ == '__main__':
    test_colourise_disabled_colour()
    test_colourise_enabled_colour()