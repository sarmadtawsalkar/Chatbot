
#!/bin/bash

echo "Welcome to online messaging platform"

echo "Created by Sc0Rpi0"

cd modules

echo "Mode Selection:"

echo "[1] Server.     [2] Client."

read -p "Please enter the appropriate number." a

if [ "$a" -eq 1 ]

then

echo "Server mode is loading...."

echo "Starting online platform for user 1"

echo "#Sc0Rpi0"

chmod +x user1.py

python user1.py

fi

if [ "$a" -eq 2 ] 

then

echo "Client mode is loading...."

echo "Starting the online platform for user 2"

echo "#Sc0Rpi0"

chmod +x  user2.py

python user2.py

fi


