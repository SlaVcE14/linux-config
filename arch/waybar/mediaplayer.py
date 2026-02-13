#!/usr/bin/env python3
import subprocess
import json

# List of media players to check
players = ["spotify", "mpv", "vlc"]

# Find the first running player
player = None
for p in players:
    try:
        status = subprocess.check_output(
            ["playerctl", "-p", p, "status"], stderr=subprocess.DEVNULL
        ).decode().strip()
        if status.lower() in ["playing", "paused"]:
            player = p
            break
    except subprocess.CalledProcessError:
        continue

if player:
    # Get title and artist
    try:
        title = subprocess.check_output(
            ["playerctl", "-p", player, "metadata", "title"], stderr=subprocess.DEVNULL
        ).decode().strip()
    except:
        title = "Unknown Title"

    try:
        artist = subprocess.check_output(
            ["playerctl", "-p", player, "metadata", "artist"], stderr=subprocess.DEVNULL
        ).decode().strip()
    except:
        artist = "Unknown Artist"

    output = {
        "text": f"{title} - {artist}",
        "icon": player
    }
    print(json.dumps(output))
else:
   print("", end="") 

