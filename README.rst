===========
django-pure
===========

.. image:: https://img.shields.io/travis/tony/django-pure.svg
   :target: https://travis-ci.org/tony/django-pure

Culmination of years of best practices accumulated using django 
on SAAS projects. No more reinventing the wheel, with `cookiecutter`_ we 
can consolidate our best practices.


Philosophy
----------

- `12 factor`_, with modifications:
  - 10. Dev/prod parity:
  
    Degrade gracefully: In absence of services on system, packages in
    environments, catch errors and continue to run. This way sites can be
    tested on local installations, staging systems without hacks.
- Python 2.7+ and 3 compatible: Python 3.x ready
- No frills: Leave the CSS / JS up to you. Only include the essentials.
  
  
.. _12 factor: http://12factor.net/

Differences from ``django-admin startproject``
----------------------------------------------

`startproject`_, ``django-admin startproject <project_name> [destination]`` 
is the tool provided in django to launch a new project. 

The `default project layout update in 1.4`_ fixed issues relating to
imports in ``manage.py``, dependencies, but allowed custom templates
for starter projects that didn't agree with the new default layout.

``django-pure`` incorporates the benefit of the new ``manage.py`` but
keeps project-specific modules adjacent to ``manage.py``. 
The `ReadTheDocs.org Django Project`_ follows this convention.

Here are the differences:

- Name of first application:

  ``startproject``: ``{{ project_name }}/{{ project_name }}``

  ``django-pure``: ``{{ project_name }}/core``

- ``ROOT_URLCONF``, ``WSGI_APPLICATION`` and ``DJANGO_SETTINGS_MODULE``
  locations:

  ``startproject``: stores ``wsgi.py``, ``urls.py`` and ``settings.py`` in 
  first app.  

  ``django-pure``: stores in project root
- ``BASE_DIR`` in settings:

  As a result of the structural change, ``BASE_DIR`` in ``settings.py``:

  ``BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))``

  to:

  ``BASE_DIR = os.path.dirname(os.path.abspath(__file__))``
- Everything in *Differences from django-admin startapp* (startappdifferences_).

  ``startproject``: Doesn't include by ``{admin,tests,views}.py`` or
  ``migrations/`` by default.

.. _default project layout update in 1.4: https://docs.djangoproject.com/en/1.8/releases/1.4/#updated-default-project-layout-and-manage-py
.. _ReadTheDocs.org Django Project: https://github.com/rtfd/readthedocs.org/tree/master/readthedocs
  
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

Split Requirements
------------------

Instead of a ``requirements.txt`` for the project, a folder,
``requirements/`` is created with:

- ``local``
- ``dev.txt``
- ``staging.txt``
- ``qa.txt``
- ``prod.txt``
  
Split Settings
--------------

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
