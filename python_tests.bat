python -m pytest python_library_demo_tests/operations_test.py::test_addition_of_two_negative_numbers
python -m pytest python_library_demo_tests
python -m pytest -m group1
python -m pytest python_library_demo_tests/mocking_test.py -s

@REM When you run pytest alone, Python uses the system’s PATH environment variable to find the pytest executable. If your Python script or module is not in a directory listed in PATH, or if there’s a problem with your Python environment, Python might not be able to locate the necessary libraries, leading to the No module named 'python_library_demo' error.

@REM On the other hand, python -m pytest tells Python to run the pytest module as a script. The -m option allows the script to be located using Python’s sys.path module search path, which includes the current directory. This is why python -m pytest can find the necessary libraries even if pytest alone cannot.

@REM -s to captured stdout section. By default, pytest captures the stdout output of the tests and only displays it if the test fails. The -s option tells pytest to display the stdout output even if the test passes.
@REM -x: exit instantly or fail fast, to stop all unit tests upon encountering the first test failure
@REM --ff: failed first, to run all tests starting from those that failed the last run
@REM -k "keyword": specify the keyword(s) to selectively run tests, can match file name or function name, and can contain and and not statements

@REM run in parallel with pytest-xdist, then use -n to specify the number of CPUs to use