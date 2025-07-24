#!/usr/bin/env bash
addr=`python3 $HOME/Scripts/pi.py`
hostname=`echo $addr|cut -d ' ' -f1`
port=`echo $addr|cut -d ' ' -f2`
username="luke"
password="1234"
expect -c "
    set timeout 5
    spawn ssh $username@$hostname -p$port
    expect {
         \"*yes/no\" { send \"yes\r\"; exp_continue }
         \"*password:\" { send \"$password\r\" }
         eof {exit}
    }
    interact
"

#expect <<EOF
#    set timeout 5
#    spawn ssh $username@$hostname -p$port
#    expect {
#         "*yes/no" { send "yes\r"; exp_continue }
#         "*password:" { send "$password\r" }
#    }
#    expect eof
#EOF
