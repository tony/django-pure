===========
django-pure
===========

This is a culmination of years of best practices accumulated using django 
on SAAS projects. No more reinventing the wheel, with `cookiecutter`_ we 
can consolidate our best practices.

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
