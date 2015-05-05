===========
django-pure
===========

Culmination of years of best practices accumulated using django 
on SAAS projects. No more reinventing the wheel, with `cookiecutter`_ we 
can consolidate our best practices.


Differences from ``django-admin startproject``
----------------------------------------------

`startproject`_, ``django-admin startproject <project_name> [destiation]`` 
is the tool provided in django to launch a new project. Here are the 
differences:

- Name of first application:

  ``startproject``: ``{{ project_name }}/{{ project_name }}``
  ``django-pure``: ``{{ project_name }}/core``

- ``ROOT_URLCONF``, ``WSGI_APPLICATION`` and ``DJANGO_SETTINGS_MODULE``
  locations:

  ``startproject``: stores ``wsgi.py``, ``urls.py`` and ``settings.py`` in 
  first app.  
  ``django-pure``: stores in project root
- As a result of keeping them in root, ``BASE_DIR`` in ``settings.py`` is
  adjusted from:

  ``BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))``

  to:

  ``BASE_DIR = os.path.dirname(os.path.abspath(__file__))``
- See startappdifferences_ for more

  ``startproject``: Doesn't include by ``{admin,tests,views}.py`` or
  ``migrations/`` by default.
  
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


.. _startproject: https://docs.djangoproject.com/en/1.8/ref/django-admin/#startproject-projectname-destination

Differences from ``django-admin startapp``
------------------------------------------

.. _startappdifferences:

Confusingly perhaps, django's default app created with ``django-admin startproject``
is not the same output as an app with ``django-admin startapp``.

``django-pure`` mixes in the ``views.py``, ``tests.py``, ``models.py``
and ``migrations/__init__.py`` into the core app.

More: `startapp`_ in django docs.

Layout comparision
~~~~~~~~~~~~~~~~~~

``django-admin startapp`` example (omitting core app)::

    project_name
    ├── second_app  <- mixed into ``startproject``'s <project_name>/<project_name> app
    │   ├── admin.py
    │   ├── __init__.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    └── manage.py


.. _startapp: https://docs.djangoproject.com/en/1.8/ref/django-admin/#startapp-app-label-destination

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
