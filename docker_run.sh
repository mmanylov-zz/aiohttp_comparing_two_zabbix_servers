#!/usr/bin/env bash

docker run --name zabbix-appliance-first -t \
      -p 10051:10051 \
      -p 1080:80 \
      -d zabbix/zabbix-appliance:latest

docker run --name zabbix-appliance-second -t \
      -p 1051:1051 \
      -p 2080:80 \
      -d zabbix/zabbix-appliance:latest