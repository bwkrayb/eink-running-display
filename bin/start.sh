#!/bin/bash
export EINK_HOME='/home/pi/eink-29'
cd $EINK_HOME
nohup /usr/bin/python3 $EINK_HOME/last-run.py > $EINK_HOME/logs/start.out 2>&1 &
