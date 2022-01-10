#!/bin/bash
export EINK_HOME='/home/pi/eink-29'
cd $EINK_HOME
nohup /usr/bin/python3 $EINK_HOME/stretch.py > $EINK_HOME/logs/stretch.out 2>&1 &
