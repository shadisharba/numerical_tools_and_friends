python -m pytest --cov
@REM to include all files in the python_library_demo_tests folder
@REM python -m pytest --cov=python_library_demo_tests
@REM python -m pytest --cov --cov-report=html:coverage_re
@REM python -m coverage report -m
@REM python -m coverage run --source=python_library_demo_tests -m pytest