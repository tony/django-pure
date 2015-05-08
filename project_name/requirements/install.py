#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Requirements auto-installer.

Installer to autodetect packages based on DJANGO_SETTINGS_MODULE and system
packages.

It can be as a command line application, or invoked from a ``manage.py``.

Environmental Variables:

"""

from __future__ import print_function

import os
import warnings

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


def _get_requirements_file(env='requirements'):
    """Return requirements file.

    If DJANGO_SETTINGS_MODULE passed in, chop off "settings." from string.

    If file doesn't exist, or doesn't exist, use "requirements.txt"
    """
    def get_path(a):
        return os.path.join(requirements_dir, "%s.txt" % a)

    if "settings." in env:
        env.replace("settings.", env)

    if os.path.isfile(get_path(env)):
        rfile = get_path(env)
    else:
        rfile = get_path('requirements')

    return rfile


def run(args):
    """Check and install application packages."""
    env = None  # Forward-declaration

    if args.settings:
        os.environ['DJANGO_SETTINGS_MODULE'] = args.settings

    # pull environment from settings name
    if 'DJANGO_SETTINGS_MODULE' in os.environ:
        env = os.environ['DJANGO_SETTINGS_MODULE'].replace("settings.", "")

    try:
        requirements_file = _get_requirements_file(env)
    except KeyError:
        warnings.warn("Requirements file %s not found." % requirements_file)

    pip.main(['install', '-r', requirements_file])


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
    )

    parser.add_argument(
        '--settings', dest='settings',
        help=("""
            The Python path to a settings module, e.g.
            "myproject.settings.main". If this isn't provided, the
            DJANGO_SETTINGS_MODULE environment variable will be
            used.
        """),
    )

    return parser

if __name__ == "__main__":
    cli_parser = _get_parser()
    cli_args = cli_parser.parse_args()

    run(cli_args)
