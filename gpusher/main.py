# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
from subprocess import call


def git_push(git_path):
    call(['/usr/bin/git', 'push', '--mirror'], cwd=git_path)
