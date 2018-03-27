# -*- coding: UTF-8 -*-
from __future__ import unicode_literals, print_function, division
import sys
from redis import Redis
from rq import Queue
from gpusher.main import git_push

q = Queue(connection=Redis())

q.enqueue(git_push, sys.argv[1])
