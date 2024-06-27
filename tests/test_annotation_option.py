from sphinx.ext.autodoc import annotation_option, SUPPRESS

def test_annotation_option_true():
    option = annotation_option(True)
    assert option == SUPPRESS

    
def test_annotation_option_false():
   option = annotation_option(False)
   assert option == False
   
if __name__ == '__main__':
    test_annotation_option_true()
    test_annotation_option_false()
