# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import sys
from subprocess import call
from redis import Redis
from rq import Queue

q = Queue(connection=Redis())


def git_push(git_path):
    call(['git push --mirror'], cwd=git_path)

q.enqueue(git_push, sys.argv[1])
