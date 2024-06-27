# Report for Assignment 1

## Project chosen

Name: Sphinx

URL: https://github.com/sphinx-doc/sphinx

Number of lines of code and the tool used to count it: 110098 NLOC

Programming language: Python

Basic installment guide:
1. `pip install sphinx`
2. `pip install defusedxml`

## Coverage measurement

### Existing tool

We used the coverage tool Pytest.

Pytest execution guide:
1. Go to the main directory
2. Execute: `pytest tests --cov=sphinx`

### Screenshots
![Screenshot part 1](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/screenshot_pytest_overall_coverage_1.png)
![Screenshot part 2](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/screenshot_pytest_overall_coverage_2.png)
![Screenshot part 3](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/screenshot_pytest_overall_coverage_3.png)
![Screenshot part 4](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/screenshot_pytest_overall_coverage_4.png)
![Screenshot part 5](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/screenshot_pytest_overall_coverage_5.png)

### Your own coverage tool

<The following is supposed to be repeated for each group member>

#### Group member: Nitesh Shahatoe
- Function 1 `terminal_supports_colour()`
- Link to commit of instrumented code: [here](https://github.com/Wavyness/sphinx/commit/37d431075016d42e5fae9e8d246806187aed0491)
- Coverage results by the instrumentation:

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/instrumentation_colour.py_prints.png)

- Function 2 `PycodeError.__str__()`
- Link of commit of instrumented code: [here](https://github.com/Wavyness/sphinx/commit/084fb6d8d42a6e5c6da7784cb80e641c2fa5b9cf)
- Coverage results by the instrumentation:

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/instrumentation_pycodeerror.prints.png)

#### Group member: Ismail Singopawiro
- Function 1 `jobs_argument()`
- Link to commit of instrumented code: [here](https://github.com/Wavyness/sphinx/commit/6f1ef04a5424bf20970e3ab843d6a0fe5d87a608)
- Coverage results by the instrumentation:

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/instrumentation_jobsarguments_prints.png)

- Function 2 `run_make_mode()`
- Link to commit of instrumented code: [here](https://github.com/Wavyness/sphinx/commit/565a4bd3a3dcee92c1fcd8afbcb9701fb3dc1b56)
- Coverage results by the instrumentation:

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/instrumentation_make_mode_prints.png)

#### Group member: Dimitri Liauw
- Function 1 `colourise()`
- Link to commit of instrumented code: [here](https://github.com/Wavyness/sphinx/commit/26b80a2bf76d109806be93b1e59e7b2a697f16e0)
- Coverage results by the instrumentation:

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/screenshot_colourise_output.png)

- Function 2 `validate_html_logo()`
- Link to commit of instrumented code: [here](https://github.com/Wavyness/sphinx/commit/b936433b7b4f69707f7e25e5edb455e37b301cda)
- Coverage results by the instrumentation:

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/instrumentation_validate_html_logo.png)

#### Group member: Riesan Hansraj
- Function 1 `annotation_option()`
- Link to commit of instrumented code: [here](https://github.com/Wavyness/sphinx/commit/590d7bb08a114211ebb35ab6008d238325191edc)
- Coverage results by the instrumentation:

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/instrumentation_annotation_prints.png)

- Function 2 `ExtensionError.category()`
- Link to commit of instrumented code: [here](https://github.com/Wavyness/sphinx/commit/e7f88539f090498a97e86e0d9fa468381a6ac015)
- Coverage results by the instrumentation:

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/instrumentation_extensionerror_prints.png)

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

### Group member Nitesh Shahatoe

Test 1 `test_terminal_support.py`
Link to commit of the new/enhanced test: [here](https://github.com/Wavyness/sphinx/commit/183bca33652a1c7af6003b1070b249b51dd2a517)

- Screenshot old coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Old-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_old_terminalsupports.png)

- Screenshot new coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![New-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_new_terminal_supports.png)

Explanation:
The coverage improved from 0% to 86% so an improvement of 86%. The old terminal_supports_colour had 10 statements.
The instrumentation gave the function 5 more statements. test_terminal_support_py calls the different branches in the function.
Calling each branch gave it a large improvement in coverage. 


Test 2 `test_pycodeError_arg.py`
Link to commit of the new/enhanced test: [here](https://github.com/Wavyness/sphinx/commit/2fe72f30421129f6e4163e64b330bf291707292c)

- Screenshot old coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Old-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_old_test_pycode_error.png)

- Screenshot new coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![New-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_new_test_pycode_error.png)

Explanation:


### Group member Ismail Singopawiro

Test 1 `test_jobsarguments.py`
Link to commit of the new/enhanced test: [here](https://github.com/Wavyness/sphinx/commit/7693264a51fad091fd77c4d30271b59df69d9738)

- Screenshot old coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_old_jobsarguments.png)

- Screenshot new coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_new_jobsarguments.png)

Test 2 `test_run_make_mode.py`
Link to commit of the new/enhanced test: [here](https://github.com/Wavyness/sphinx/commit/fb1b43c45a221e09c32b29a2425fb5f57bcf4b32)

- Screenshot old coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Old-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_old_make_mode.png)

- Screenshot new coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![New-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_new_make_mode.png)

### Group member Dimitri Liauw

Test 1 `test_colourise.py`
Link to commit of the new/enhanced test: [here](https://github.com/Wavyness/sphinx/commit/36b4b7132fde923dbf8dd9605bcc769849114c2c)

- Screenshot old coverage

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_old_colourise.png)

- Screenshot new coverage

![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_new_colourise.png)

Test 2 `test_validate_html_logo.py`
Link to commit of the new/enhanced test: [here](https://github.com/Wavyness/sphinx/commit/9c2d41e7054d75dcf06ad31c8141a2c33273205d)

- Screenshot old coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Old-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_old_validate_html_logo.png)

- Screenshot new coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![New-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_new_validate_html_logo.png)

### Group member Riesan Hansraj

Test 1 `test_annotation_option.py`
Link to commit of the new/enhanced test: [here](https://github.com/Wavyness/sphinx/commit/2f0837c6198f25ca502821ec55e57cad0c50a85f)

- Screenshot old coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Old-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_old_annotation_option.png)

- Screenshot new coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![New-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_new_annotation_option.png)

Explanation:
the code coverage improved by 100%.

the first step was to make the instrumentation to see which branches it would hit. and also which values would make sure it would hit.
after that. the new test file was created with the information of the branch test.
the test used assertions to control the results.

Test 2 `test_extensionerror_category.py`
Link to commit of the new/enhanced test: [here](https://github.com/Wavyness/sphinx/commit/85899c0d236958b2d2dd3ad1b2caf486f706c151)

- Screenshot old coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![Old-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_old_extensionerror.png)

- Screenshot new coverage

![Header](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/html_file_layout.png)
![New-Cov](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/coverage_results/coverage_new_test_extensionerror.png)

Explanation:
the code coverage of the second function was also improved by 100%

the way the second function was improved was almost the same as the first one.
there was again no test file testing the function so a new test file was created to make sure 
the function was called and tested based on the branch test performed.

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

A significant portion of our assignment was spent searching for the right project. This process took a lot of time due to numerous restrictions and the fact that many good projects were already taken. After weeks of searching together, we finally found a suitable project.

Each team member identified and created two functions to instrument, and everyone also developed two tests for these functions. We communicated through out Discord, which helped us avoid communication issues and ensured that everyone contributed their fair share of work.
