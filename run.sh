#!/bin/bash
PORT=9090
if [ ! -d "env" ]; then
    echo "Virtual environment does not exist, thus net server was never built, run install.sh"
    exit 1
fi

source ./env/Scripts/activate
if ! [ -x "$(command -v net-server)" ]; then
    echo "net-server program could not be found, run install.sh"
    exit 1
fi

echo "Starting server, url will be localhost:9090"
echo "Use Ctrl + C to quit server, may take a second to stop."
net-server $PORT