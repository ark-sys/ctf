#!/usr/bin/env bash

PATH=$(/usr/bin/getconf PATH || /bin/kill $$)

PASS=$(cat .passwd)

if [ ! -v "$1" ]; then
    echo "nope"
    exit 1
fi


if test "$1" = "$PASS" 2>/dev/null  ; then
    echo "Well done you can validate the challenge with : $PASS"
else
    echo "Try again ,-)"
fi

exit 0

