#!/bin/bash
export EINK_HOME='/home/pi/eink-29'
cd $EINK_HOME
nohup /usr/bin/python3 $EINK_HOME/month-stats.py > $EINK_HOME/logs/monthly.out 2>&1 &
