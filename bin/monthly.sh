#!/bin/bash
export EINK_HOME='/home/pi/eink-running-display'
export EINK_ENV='/home/pi/eink-running-display/.venv/bin'
cd $EINK_HOME
nohup $EINK_ENV/python3 $EINK_HOME/month-stats.py > $EINK_HOME/logs/monthly.out 2>&1 &
