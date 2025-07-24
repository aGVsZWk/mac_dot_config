#!/bin/bash
# 没有参数
# position="大恒科技大厦"
# position="赵陵铺镇"
# position="蔡村乡"
position="北京体育大学"
if [ $# -eq 0 ]
then
    curl -s "http://wttr.in/$position?lang=zh" | sed '1d' |sed '$d'
    exit 0
fi

# 参数1：天数 
if [ "$1" -gt 0 ] 2>/dev/null && [ $# -eq 1 ] 
then
    if [ $1 -gt 3 ]
    then
        echo "天数必须小于等于3"
        exit 1
    fi
    curl -s "http://wttr.in/$position?&lang=zh&${1}" | sed '1d' |sed '$d'

    exit 0
fi

# 参数1：城市
if ! [ "$1" -gt 0 ] 2>/dev/null && [ $# -eq 1 ] 
then
    curl -s "http://wttr.in/$1?lang=zh" | sed '1d' |sed '$d'
    exit 0
fi


# 参数1：天数  参数2：城市
if [ "$2" -gt 0 ] 2>/dev/null && [ $# -eq 2 ]
then
    curl -s "http://wttr.in/${1}?${2}&lang=zh" | sed '1d' |sed '$d'
    exit 0
else
    echo "参数错误！！"
    exit 1
fi




