#!/usr/bin/env bash

BASEDIR=$(dirname "$0")
source ${BASEDIR}/.env/bin/activate
python ${BASEDIR}/enqueue.py $@