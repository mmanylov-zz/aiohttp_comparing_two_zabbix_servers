#!/usr/bin/env bash

docker run --name zabbix-appliance -t \
      -p 10051:10051 \
      -p 1080:80 \
      -d zabbix/zabbix-appliance:latest

