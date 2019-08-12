#!/usr/bin/env bash

cd server

source ./venv/bin/activate

flask run --host 0.0.0.0 --without-threads
