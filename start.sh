#!/usr/bin/env bash

if [ ! -f start.sh ]; then
    echo working directory does not exist start.sh
    exit 1
fi

if [ ! -d .env ]; then
    virtualenv .env
fi

source .env/bin/activate

pip install -r requirements.txt
echo $(pwd)/src > .env/lib/python2.7/gpusher.pth
if [ $(ps -Af | grep redis | grep -v grep | wc -l) -eq 0 ]; then
    echo redis is not running
    exit 1
fi
rqworker &