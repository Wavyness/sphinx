from sphinx.errors import ExtensionError

def test_with_modname():
    error = ExtensionError("An extension error occurred", modname="mod")
    category = error.category
    assert category == "Extension error (mod)", f"Expected 'Extension error (mod)', but got {category}"
    print("With modname:", category)

def test_without_modname():
    error = ExtensionError("An extension error occurred")
    category = error.category
    assert category == "Extension error", f"Expected 'Extension error', but got {category}"
    print("Without modname:", category)


if __name__ == '__main__':
    test_with_modname()
    test_without_modname()