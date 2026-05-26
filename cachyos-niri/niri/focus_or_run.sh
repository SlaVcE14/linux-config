#!/bin/bash
# Usage: ./niri-focus-or-launch.sh <app_id>
APP=$1

# Find the window ID of the application if it is running
WINDOW_ID=$(niri msg -j windows | jq -r ".[] | select(.app_id == \"$APP\") | .id" | head -n 1)

if [ -n "$WINDOW_ID" ]; then
    # Window exists: Focus it
    niri msg action focus-window --id "$WINDOW_ID"
else
    # Window does not exist: Launch it
    niri msg action spawn -- "$APP"
fi
