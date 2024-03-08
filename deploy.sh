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
    nohup python3 app.py > /dev/null 2>&1 &
    disown
    echo "Start success"
}
stop() {
    echo "Stoping..."
    ps -ef | grep "python3 app.py" | grep -v grep | awk '{print $2}' | xargs kill -9
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