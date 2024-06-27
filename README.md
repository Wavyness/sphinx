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

### Group member: Nitesh
Function 1 `terminal_supports_colour()`

Link to commit of instrumented code: https://github.com/sphinx-doc/sphinx/commit/37d431075016d42e5fae9e8d246806187aed0491


<Provide a screenshot of the coverage results output by the instrumentation>
### Screenshot coverage results:
![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/instrumentation_colour.py_prints.png)

<Function 2 name>

<Provide the same kind of information provided for Function 1>

### Group member: Ismail
Function 1 `jobs_argument()`

Link to commit of instrumented code: https://github.com/sphinx-doc/sphinx/commit/6f1ef04a5424bf20970e3ab843d6a0fe5d87a608
### Screenshot coverage results:
![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/screenshot_job_arguments_output.png)


### Group member: Dimitri
Function 1 `colourise()`

Link to commit of instrumented code: https://github.com/sphinx-doc/sphinx/commit/26b80a2bf76d109806be93b1e59e7b2a697f16e0
### Screenshot coverage results:
![Screenshot](https://github.com/Wavyness/sphinx/blob/master/doc/screenshots/screenshot_colourise_output.png)



## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
