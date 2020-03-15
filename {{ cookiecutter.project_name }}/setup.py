#!/usr/bin/env python

# Standard library modules.
import os
import sys
import logging

# Third party modules.
from setuptools import setup, find_packages

# Local modules.
import versioneer

# Globals and constants variables.
logger = logging.getLogger(__name__)
BASEDIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(BASEDIR, 'README.md'), 'r') as fp:
    LONG_DESCRIPTION = fp.read()

PACKAGES = find_packages()

with open(os.path.join(BASEDIR, 'requirements.txt'), 'r') as fp:
    INSTALL_REQUIRES = fp.read().splitlines()

EXTRAS_REQUIRE = {}
with open(os.path.join(BASEDIR, 'requirements_dev.txt'), 'r') as fp:
    EXTRAS_REQUIRE['dev'] = fp.read().splitlines()

CMDCLASS = versioneer.get_cmdclass()

ENTRY_POINTS = {}

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name='{{ cookiecutter.project_name }}',
    version=versioneer.get_version(),
    url='https://github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_name }}',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    description="{{ cookiecutter.project_short_description }}",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
{%- if cookiecutter.license in license_classifiers %}
    license="{{ cookiecutter.license }}",
{%- endif %}

    packages=PACKAGES,
    include_package_data=True,

    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,

    cmdclass=CMDCLASS,

    entry_points=ENTRY_POINTS,
)

