=====
Notes
=====


FreeBSD
-------


SQLite Error::

    django.core.exceptions.ImproperlyConfigured: Error loading either
    pysqlite2 or sqlite3 modules (tried in that order): No module named
    _sqlite3

Solution::
    
    $ pkg install py27-sqlite3
