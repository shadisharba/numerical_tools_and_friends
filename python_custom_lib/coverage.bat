python -m pytest --cov --cov-report=xml:./reports/coverage/coverage.xml
@REM to include all files in the tests folder
@REM python -m pytest --cov=tests
@REM python -m pytest --cov --cov-report=html:coverage_re
@REM python -m coverage report -m
@REM python -m coverage run --source=tests -m pytest