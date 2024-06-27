from unittest.mock import Mock
from sphinx.builders.html import validate_html_logo
import os

app = Mock()
app.confdir = os.getcwd() 
config = Mock()

def test_validate_logo_none():
    config.html_logo = None
    assert None == validate_html_logo(app, config)

def test_validate_logo():
    config.html_logo = 'non_existing_logo.png'
    assert None == validate_html_logo(app, config)

if __name__ == '__main__':
    test_validate_logo_none()
    test_validate_logo()