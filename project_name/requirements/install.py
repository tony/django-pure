#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Requirements auto-installer.

Installer to autodetect packages based on DJANGO_SETTINGS_MODULE and system
packages.

It can be as a command line application, or invoked from a ``manage.py``.

Arguments:

    --force
        continue installation of packages even if required system command not
        found in PATHs

Environmental Variables:

    DJANGO_SETTINGS_MODULE
        Will process settings.foo to requirements/foo.txt, will install if
        exists.
"""

from __future__ import print_function

import os

try:
    import pip
except ImportError:
    print(
        "You must install pip.\n"
        "See https://pip.pypa.io/en/latest/installing.html"
    )


def _which(exe=None, throw=True):
    """Return path of bin. Python clone of /usr/bin/which.

    from salt.util - https://www.github.com/saltstack/salt - license apache

    :param exe: Application to search PATHs for.
    :type exe: string
    :param throw: Raise ``Exception`` if not found in paths
    :type throw: bool
    :rtype: string

    """
    if exe:
        if os.access(exe, os.X_OK):
            return exe

        # default path based on busybox's default
        default_path = '/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin'
        search_path = os.environ.get('PATH', default_path)

        for path in search_path.split(os.pathsep):
            full_path = os.path.join(path, exe)
            if os.access(full_path, os.X_OK):
                return full_path

        message = (
            '{0!r} could not be found in the following search '
            'path: {1!r}'.format(
                exe, search_path
            )
        )

        if throw:
            raise Exception(message)
        else:
            print(message)
    return None


requirements_dir = os.path.dirname(os.path.abspath(__file__))

requirements = {
    "local": os.path.join(requirements_dir, "local.txt")
}


def run(*args, **kwargs):
    """Check and install application packages."""
    print(args, kwargs)
    pip.main(['install', '-r', requirements['local']])


def _get_parser():
    """Return :class:`argparse.ArgumentParser`."""
    import argparse

    parser = argparse.ArgumentParser(
        description=__doc__
    )

    parser.add_argument(
        '-f', '--force', dest='force',
        help='Force installation of packages.',
        action='store_true',
        default=False
    )

    return parser

if __name__ == "__main__":
    cli_parser = _get_parser()
    cli_args = cli_parser.parse_args()

    run(cli_args)
