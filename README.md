# Setup dependencies for pip

1. `pip install twine`
2. `pip install wheel`

# How to publish to pip

1. `python setup.py sdist`
2. `python setup.py bdist_wheel --universal`
3. `twine upload dist/*`