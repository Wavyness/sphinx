from sphinx.cmd.make_mode import run_make_mode

def test_run_make_mode_1():
    result = run_make_mode(["gettext"])
    assert result == 1

def test_run_make_mode_3wrong():
    result = run_make_mode(["a", "b", "c"])
    assert result == 2

if __name__ == '__main__':
    test_run_make_mode_1()
    test_run_make_mode_3wrong()
