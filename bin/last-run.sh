#!/bin/bash
export EINK_HOME='/home/pi/eink-29'
cd $EINK_HOME
nohup /usr/bin/python3 $EINK_HOME/lg-last-run.py > $EINK_HOME/logs/last-run.out 2>&1 &
