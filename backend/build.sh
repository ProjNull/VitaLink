#!/bin/bash

if  [ -f "clean.sh" ]; then
    echo Found a clean script! Running it...
    ./clean.sh
else
    echo No clean script found. If you want to run a snippet before building, create a file named clean.sh and make it executable.
fi

# Check if the first argument is "dev"
if ! command -v gunicorn &> /dev/null; then
    alias gunicorn="python3 -m gunicorn"
    if ! command -v gunicorn &> /dev/null; then
        alias gunicorn="python -m gunicorn"
        if ! command -v gunicorn &> /dev/null; then
            echo gunicorn is not installed!
            exit 1
        fi
    fi
fi

gunicorn --version

if [ "$1" == "dev" ]; then
    if [ "$2" == "public" ]; then
        gunicorn app:app --reload --host 0.0.0.0 --port 8000
    else
        gunicorn app:app --reload --port 8000
    fi
else
    if [ "$1" == "test" ]; then
        pytest tests/
    else
        gunicorn app:app --host 0.0.0.0 --port 8000
    fi
fi
