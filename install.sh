#!/bin/bash

if [ ! -d "env" ]; then
    echo "Virtual environment does not exist, creating one with name env"
    python -m venv env
fi

source ./env/Scripts/activate
pip install tox
tox
pip install ./.tox/dist/server*.zip
echo "Program net-server built and local installed."
