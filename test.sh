#!/bin/bash
echo “Testing lambda”
export PATH=$PATH:/Users/mccurrs/Documents/Workspaces/slack-cloudwatch/venv/bin
python-lambda-local -f $1 $2 $3
