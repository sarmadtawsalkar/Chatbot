#!/usr/bin/python

import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host=input('Enter the ip address:')

port=input('Enter the port address:')

print('Client is initiated')

port=int(port)

s.connect((host,port))

print('Welcome to the online messaging platform')


i = 0

while (i<100):

  print('User1#:')

#  print('Wait for User1 to reply')
  msg=s.recv(10)

  print(msg.decode('ascii'))

  pass 

  msg1=input('User2:#\n') 
 # print('Type your message User2')
  s.send(msg1.encode('ascii'))

  pass
  
  i += 1

