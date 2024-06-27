from sphinx.errors import PycodeError

def pycode_error_1_argument():
    error_1_arg = PycodeError("error")
    print("WITH 1 ARGUMENT")
    print(error_1_arg)
    assert str(error_1_arg) == "error"

def pycode_error_with_2_arguments():
    error_2_arg = PycodeError("error","exception")
    print("WITH 2 ARGUMENTS")
    print(error_2_arg)
    assert str(error_2_arg) == "error (exception was: 'exception')"



if __name__ == '__main__':
    pycode_error_1_argument()
    pycode_error_with_2_arguments()