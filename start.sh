#!/bin/bash

usage() {
    echo "Missing params..."
    echo "Usage: ./start.sh <TIMES_TO_REPEAT> <USER_WORDLIST>"
}

start() {
    echo "Ok"
    repeat_times=$1
    wordlist=$2

    echo "repeat_times = $repeat_times"
    echo "wordlist = $wordlist"

    for line in $(cat $wordlist); do
        echo -e "\n\n------- USER: $line -------"
        for i in $(seq 1 $repeat_times); do
            python3 ./index.py $line
        done
    done
}

if [ -z "$1" -o -z "$2" ];
then
    usage
    exit
else
    repeat_times=$1
    wordlist=$2

    start $repeat_times $wordlist
fi