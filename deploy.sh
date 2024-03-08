#!/bin/bash

cd $(dirname $0)

ACTION=$1

usage() {
    echo "Usage: $PROG_NAME {start|stop|restart}"
    exit 2
}

start() {
    echo "Starting..."
    source /root/server-env/bin/activate
    python3 app.py
}
stop() {
    echo "Stoping..."
    # Find the process ID of the Python script and send it a termination signal
    PID=$(pgrep -f "python3 app.py")
    if [ -n "$PID" ]; then
        kill "$PID"
        echo "Server stopped."
    else
        echo "Server is not running."
    fi
}
case "$ACTION" in
    start)
        start
    ;;
    stop)
        stop
    ;;
    restart)
        stop
        start
    ;;
    *)
        usage
    ;;
esac