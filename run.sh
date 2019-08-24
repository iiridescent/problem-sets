#!/bin/sh

tmux new-session -d './server.sh'
tmux split-window -v './client.sh'
tmux -2 attach-session -d
