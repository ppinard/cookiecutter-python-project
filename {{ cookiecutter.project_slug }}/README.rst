{% for _ in cookiecutter.project_name %}={% endfor %}
{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

.. image:: https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}.svg
        :target: https://pypi.python.org/pypi/{{ cookiecutter.project_slug }}

.. image:: https://img.shields.io/travis/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.svg
        :target: https://travis-ci.org/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}

.. image:: https://readthedocs.org/projects/{{ cookiecutter.project_slug | replace("_", "-") }}/badge/?version=latest
        :target: https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

{{ cookiecutter.project_short_description }}


Installation
============

Easiest way to install using ``pip``::

    pip install {{ cookiecutter.project_slug }}

For development installation from the git repository::

    git clone git@github.com/{{ cookiecutter.github_organization }}/{{ cookiecutter.project_slug }}.git
    cd {{ cookiecutter.project_slug }}
    pip install -e .

Release notes
=============

0.1.0
-----


Contributors
============


License
=======

The library is provided under the {{ cookiecutter.license }} license.

Copyright (c) {% now 'local', '%Y' %}, {{ cookiecutter.full_name }}





