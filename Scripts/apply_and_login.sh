#!/bin/bash
al="/usr/local/bin/python3 /Users/kj/Scripts/apply_login.py"
lg="/usr/bin/expect /Users/kj/Scripts/login.exp"

allg()
{
    ip=$1
    $al $ip
    $lg $ip
}

allg $1

