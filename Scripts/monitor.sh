#!/bin/bash
sudo tcpdump -vvv   port 50000 or port 50002 or port 56100 or port 56101 -w cap_monitor 2>&1 &
