#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ) as fh:
        return fh.read()


setup(
    name='kotonoha',
    version='0.4.1',
    license='MIT license',
    description='Tools for preprocessing Japanese texts',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Bruno Toshio Sugano',
    author_email='brunotoshio@gmail.com',
    url='https://github.com/brunotoshio/kotonoha',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
    project_urls={
        'Documentation': 'https://kotonoha.readthedocs.io/',
        'Changelog': 'https://kotonoha.readthedocs.io/en/latest/changelog.html',
        'Issue Tracker': 'https://github.com/brunotoshio/kotonoha/issues',
    },
    keywords=[
        'japanese', 'textprocessing', 'nlp',
    ],
    python_requires='~=3.6',
    install_requires=[
        'jaconv==0.2.4'
    ],
)
