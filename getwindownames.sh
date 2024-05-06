#!/bin/bash

# Get the window IDs of all visible windows
window_ids=$(xdotool search --onlyvisible --name ".*")

# Loop through each window ID and get its name
for id in $window_ids; do
    window_name=$(xdotool getwindowname $id)
    echo "Window ID: $id, Name: $window_name"
done