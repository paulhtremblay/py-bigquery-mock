set -e
python setup.py check
python setup.py sdist
python setup.py bdist_wheel --universal
#twine upload --repository testpypi dist/*
twine upload -r pypi dist/*
