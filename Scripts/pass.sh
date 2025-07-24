#!/bin/bash
if [ $1 == "xhy" ];then
    if [ $# -ge 2 ] && [ $2 == "rpc" ]; then
        /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome "http://paas.yingzhongtong.com/ui/#/ticket/risksystem.technical_output.external_risk_rpc/ars/assemlines"
    else
        /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome "http://paas.yingzhongtong.com/ui/#/ticket/risksystem.technical_output.external_risk_policy_xhy/ars/assemlines"
    fi
fi
if [ $1 == "xf" ];then
    if [ $# -ge 2 ] && [ $2 == "rpc" ]; then
        /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome "http://paas.yingzhongtong.com/ui/#/ticket/risksystem.technical_output.risk_rpc/ars/assemlines"
    else
        /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome "http://paas.yingzhongtong.com/ui/#/ticket/risksystem.technical_output.xfkj_fraud/ars/assemlines"
    fi
fi
