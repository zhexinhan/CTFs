#!/usr/bin/python3.6

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('73.35.192.140', 80))
s.listen(1)
conn, addr = s.accept()
if conn.recv(10000).find('GET hanzx1994/hanzx1994.html HTTP/1.1') != -1:
    conn.sendall('My name is hanzx1994 and iChall.')
