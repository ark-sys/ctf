#!/usr/bin/env bash

set -o pipefail

mkfifo fifo
./crack.py < fifo | ./test.py | tee fifo
rm -f fifo