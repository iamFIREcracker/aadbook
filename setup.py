#!/usr/bin/env python

import os
from setuptools import find_packages
from setuptools import setup

from aadbook import __version__


VERSION = __version__
NAME = 'aadbook'
PACKAGES = [NAME]
DESCRIPTION = 'AADBook -- Access your Azure AD contacts from the command line'
readme = os.path.join(os.path.dirname(__file__), 'README.rst')
LONG_DESCRIPTION = open(readme).read()
INSTALL_REQUIRES = [
    'adal==1.0.2',
    'requests==2.19.1'
]

URL = 'https://bitbucket.org/iamFIREcracker/aadbook'
DOWNLOAD_URL = 'http://pypi.python.org/pypi/aadbook'

CLASSIFIERS = [  # XXX review these
    'Development Status :: 4 - Beta',
    'Environment :: Other Environment',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.2',
    'Topic :: Text Processing :: Filters',
    'Topic :: Utilities',
]

AUTHOR = 'Matteo Landi'
AUTHOR_EMAIL = 'matteo@matteolandi.net'
KEYWORDS = "contacts azure ad mutt".split(' ')

params = dict(
    name=NAME,
    version=VERSION,
    packages=find_packages(),
    entry_points={
        'console_scripts': ['aadbook = aadbook.aadbook:_main'],
    },
    install_requires=INSTALL_REQUIRES,

    # metadata for upload to PyPI
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    license='BSD',
    keywords=KEYWORDS,
    url=URL,
    download_url=DOWNLOAD_URL,
    classifiers=CLASSIFIERS,
)

setup(**params)
