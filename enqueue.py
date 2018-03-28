# -*- coding: UTF-8 -*-

import sys
from redis import Redis
from rq import Queue
from gpusher.main import git_push

q = Queue(connection=Redis())

q.enqueue(git_push, sys.argv[1])
