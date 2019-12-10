python -m coverage run --source=peacemakr_sdk/impl/models,peacemakr_sdk/impl example.py > /dev/null
python -m coverage report -m > output/coverage/coverage_report.txt
python -m coverage html
mv htmlcov/* output/coverage/

flake8 --format=html --htmldir=output/flake8 example.py peacemakr_sdk/*.py peacemakr_sdk/impl/*.py

pytest --html=pytest.html --self-contained-html
mv pytest.html output/tests/
