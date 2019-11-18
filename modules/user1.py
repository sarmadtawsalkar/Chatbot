#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=input('Enter the ip address:')

port=input('Enter the port number:')

port=int(port)

print('Server is initiated\nWait for Client to response')

s.bind((host,port))

s.listen(5)

c,addr=s.accept()

print('Welcome to the Messenging platform')

print('#Sc0Rpi0')

print('Connection from ',addr)

print('Starting........')

i = 0

while (i<100):

  msg=input('User1:#\n')
#  print('User1 type your message')
  c.send(msg.encode('ascii'))

  pass

  print('User2:#')
 # print('Wait for User2 to reply')
  msg1=c.recv(10)
  print(msg1.decode('ascii'))

  pass

  i += 1
