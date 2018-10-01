# Release

Update the version inside 'aadbook/__init__.py'.

Remove 'dist/' directory:

    rm -rf dist/*

Generate the next build:

    python setup.py sdist

Publish it to Test PyPi:

    twine upload dist/* -r testpypi

Publish it to PyPi:

    twine upload dist/* -r pypi
