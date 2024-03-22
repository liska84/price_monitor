#!/bin/bash
# Start Xvfb
Xvfb :99 -screen 0 1920x1080x24 &
export DISPLAY=:99

# Start cron service
cron

# Keep the container running by tailing logs or another long-running process
tail -f /dev/null