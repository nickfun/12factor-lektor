#!/bin/bash
D=`date`
cat ./databags/misc.ini.template | sed -e "s/ZZZ/$D/g" > ./databags/misc.ini
time lektor build -O ./docs
