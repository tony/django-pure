===========
django-pure
===========

This is a culmination of years of best practices accumulated using django 
on SAAS projects. No more reinventing the wheel, with `cookiecutter`_ we 
can consolidate our best practices.


Differences from ``django-admin startproject``
----------------------------------------------

``djangoadmin startproject <project_name>`` is the tool provided in django
to launch a new project. Here are the differences:

- ``startproject`` creates a project and a first application with the same
  name. ``{{ project_name }}/{{ project_name }}``.
  
  ``django-pure`` uses ``{{ project_name }}/core`` for the first app.
- ``startproject`` will keep the wsgi, urls and settings module inside
  the first app.
  
  ``django-pure``: Keeps urls, wsgi and settings in the root of the project
- As a result of keeping them in root, ``BASE_DIR`` in ``settings.py`` is
  adjusted from:

  ``BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))``

  to:

  ``BASE_DIR = os.path.dirname(os.path.abspath(__file__))``
- ``startproject`` will not include ``views.py``, ``tests.py``, ``admin.py``
  and ``migrations/`` in the same app.

  ``django-pure``: adds boilerplate from ``startapp core`` for the
  initial app, which includes ``views``, ``tests`` and ``admin``
  module.
  
  
Layout comparision
~~~~~~~~~~~~~~~~~~

``django-admin startproject``::

    project_name
    ├── db.sqlite3
    ├── project_name
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   └── wsgi.py
    └── manage.py

``django-pure``::

    project_name
    ├── core
    │   ├── admin.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── db.sqlite3
    ├── manage.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

Roadmap
-------

- No bootstrap / css / js frameworks.
- Django 1.8
- Python 2.7 + 3.4 support
- Salt
- Fabric -> Salt-SSH
- Vagrant
- Graceful degradation to sqlite in local instances.
- Example tests using ``RequestFactory``.
- tmuxp configuration and ``bootstrap_env.py`` to launch CLI workspaces,
  as well as TDD.
- License: MIT, use in your open source, personal or commercial projects
  as you see fit.
  
.. _cookiecutter: https://github.com/audreyr/cookiecutter
